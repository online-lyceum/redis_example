from redis import Redis
import logging


logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
redis = Redis(host="redis", port=6379)

logger.info("DEL Key")
redis.delete("Key")
logger.info(f"{redis.get('Key')=}")
logger.info("SET Key Value")
redis.set("Key", "Value")
logger.info(f"{redis.get('Key')=}")

redis.close()
