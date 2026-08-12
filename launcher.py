"""
SowardBot Launcher - Starts both the Discord bot and API server
This file is the entry point for the .EXE build
"""
import asyncio
import discord
import discord.http
import uvicorn
import os
import sys
from pathlib import Path
from threading import Thread

# Add the project root to the path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from core.Bot import AutoShardedBot
from settings.config import BotConfigClass
from services.logging import logger

BotConfig = BotConfigClass()

# Validate Discord token
if not BotConfig.TOKEN:
    logger.error("❌ Discord bot token not configured!")
    logger.error("Please edit .env file and add your Discord bot token")
    logger.error("Get your token from: https://discord.com/developers/applications")
    sys.exit(1)

# Create bot instance
bot = AutoShardedBot()


async def main():
    """Main entry point that starts both bot and API server"""
    try:
        from modules.sync import loadDataBase
        from modules.cache import load_cache
        from api import api
        
        logger.info("Initializing SowardBot...")
        try:
            await loadDataBase()
            await load_cache()
            logger.info("Database and cache initialized successfully ✅")
        except Exception as e:
            logger.warning(f"Database initialization failed: {e}")
            logger.warning("Bot will run in limited mode without database features")
        
        try:
            await bot.load_extension("cogs")
            logger.info("Bot extensions loaded successfully")
        except Exception as e:
            logger.warning(f"Some extensions failed to load: {e}")
            logger.info("Bot will continue with available extensions")

        tasks = []

        async def start_bot():
            """Start the Discord bot"""
            try:
                logger.info("Starting Discord bot...")
                await bot.start(BotConfig.TOKEN, reconnect=True)
            except KeyboardInterrupt:
                logger.error("Bot has been stopped")
            except discord.RateLimited as e:
                logger.error(f"Bot is rate limited. Retrying in {e.retry_after} seconds")
            except discord.LoginFailure as e:
                logger.error(f"Login failed. {e}")
            except discord.HTTPException as e:
                retry_after = e.response.headers.get('Retry-After', 'N/A')
                logger.error(f"Bot is rate limited. Retrying in {retry_after} seconds")
                if retry_after == 'N/A':
                    return
                logger.error(f"Rate limit details: {e.response.status} {e.response.reason}")
                logger.error(f"Response headers: {e.response.headers}")
                logger.error(f"Response text: {e.status} {e.text}")
                await asyncio.sleep(int(retry_after))

        async def start_api():
            """Start the FastAPI server"""
            try:
                # Use Railway's PORT if available, otherwise use API_PORT or default to 3000
                api_port = int(os.getenv('PORT', os.getenv('API_PORT', 3000)))
                api_host = os.getenv('API_HOST', '0.0.0.0')
                logger.info(f"Starting API server on {api_host}:{api_port}...")
                config = uvicorn.Config(
                    app="api.api:app",
                    host=api_host,
                    port=api_port,
                    log_level="info",
                    access_log=True,
                )
                server = uvicorn.Server(config)
                await server.serve()
            except Exception as e:
                logger.error(f"API server failed to start: {e}")

        # Start both tasks
        tasks.append(asyncio.create_task(start_bot()))
        tasks.append(asyncio.create_task(start_api()))

        await asyncio.gather(*tasks)

    except Exception as e:
        logger.error(f"Fatal error during startup: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    logger.info("=" * 50)
    logger.info("SowardBot Launcher Started")
    logger.info("=" * 50)
    
    # Handle Windows event loop
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Shutdown signal received. Exiting...")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
