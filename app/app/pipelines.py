
from itemadapter import ItemAdapter
from typing import Any



class AppPipeline:
    def process_item(self, item, spider) -> Any:
        return item
