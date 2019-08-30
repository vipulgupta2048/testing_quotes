from spider_test.items import TestItem1, TestItem2

BOT_NAME = "spider_test"

SPIDER_MODULES = ["spider_test.spiders"]
NEWSPIDER_MODULE = "spider_test.spiders"
ROBOTSTXT_OBEY = True

EXTENSIONS = {"spidermon.contrib.scrapy.extensions.Spidermon": 500}

ITEM_PIPELINES = {"spidermon.contrib.scrapy.pipelines.ItemValidationPipeline": 800}

SPIDERMON_ENABLED = True

# Ways to add Cerberus schemas for testing Cerberus Validation

# 2 items from Scrapy, 2 seperate schemas
# SPIDERMON_VALIDATION_CERBERUS = {
#     TestItem1:'/home/vipulgupta2048/quotes/spider_test/schema.json',
#     TestItem2:'/home/vipulgupta2048/quotes/spider_test/quotes.json'
#     }

# Absolute path to schema
# SPIDERMON_VALIDATION_CERBERUS = ['/home/vipulgupta2048/quotes/spider_test/schema.json']

# Prasing schemas from URL
# SPIDERMON_VALIDATION_CERBERUS = ['https://api.myjson.com/bins/gmdgl']

# Providing scheama directly
# SPIDERMON_VALIDATION_CERBERUS = [{
#     "quote": {"type": "string", "required": True},
#     "author": {"type": "number", "required": True},
#     "author_url": {"type": "string"},
#     "tags": {"type": "list"}
# }]

# Adds errors to items, check output
SPIDERMON_VALIDATION_ADD_ERRORS_TO_ITEMS = True

# Testing Schematics
# SPIDERMON_VALIDATION_MODELS = (
#     'placement.validators.Product',
# )

# SPIDERMON_SPIDER_CLOSE_MONITORS = (
#     'placement.monitors.SpiderCloseMonitorSuite',
# )

# Testing JSONSchema
# SPIDERMON_VALIDATION_SCHEMAS = ['/home/vipulgupta2048/quotes/spider_test/quotes.json']
