BOT_NAME = "spider_test"

SPIDER_MODULES = ["spider_test.spiders"]
NEWSPIDER_MODULE = "spider_test.spiders"
ROBOTSTXT_OBEY = True

EXTENSIONS = {"spidermon.contrib.scrapy.extensions.Spidermon": 500}

ITEM_PIPELINES = {"spidermon.contrib.scrapy.pipelines.ItemValidationPipeline": 800}

SPIDERMON_ENABLED = True

# Three ways to add schemas working

SPIDERMON_VALIDATION_CERBERUS = ['/home/vipulgupta2048/quotes/spider_test/schema.json']
# SPIDERMON_VALIDATION_CERBERUS = ['https://api.myjson.com/bins/gmdgl']
# SPIDERMON_VALIDATION_CERBERUS = [{
#     "quote": {"type": "string", "required": True},
#     "author": {"type": "string", "required": True},
#     "author_url": {"type": "string"},
#     "tags": {"type": "list"}
# }]

# SPIDERMON_VALIDATION_ADD_ERRORS_TO_ITEMS = True


# SPIDERMON_VALIDATION_MODELS = (
#     'placement.validators.Product',
# )

# SPIDERMON_SPIDER_CLOSE_MONITORS = (
#     'placement.monitors.SpiderCloseMonitorSuite',
# )

# SPIDERMON_VALIDATION_SCHEMAS = ['/home/vipulgupta2048/quotes/spider_test/quotes.json']
