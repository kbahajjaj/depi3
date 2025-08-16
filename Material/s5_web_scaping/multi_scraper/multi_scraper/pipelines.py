from datetime import datetime
from itemadapter import ItemAdapter

class AddTimestampPipeline:
    """
    Simple pipeline to add 'scraped_at' field to each item.
    """
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter["scraped_at"] = datetime.utcnow().isoformat(timespec="seconds") + "Z"
        return item
    
