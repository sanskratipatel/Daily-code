



from motor.motor_asyncio import AsyncIOMotorClient
import asyncio


MONGO_URI = (
    "mongodb://admin:TExrCPC!%2B%3DUZx%25Tmd9%7D4@beta.mongoserver.ko-tech.in:27017/"
    "?authSource=admin&directConnection=true&tls=true"
)

DB_NAME = "CRM-Database"

mongo_client = AsyncIOMotorClient(MONGO_URI)
mongo_db = mongo_client[DB_NAME]


def get_mongo_db():
    return mongo_db





async def get_filter_type_mongo(
    order_ids: list[str],
    # picklist_id: int,
    # connection: AsyncConnection
):
    """
    Determine filter type (B2B, B2C, MIX) per order from Mongo
    and update picklist_order_details.
    Returns mapping of order_id -> filter
    """

    
    db = get_mongo_db()
    coll = db["orders"]

    order_filter_map: dict[str, str] = {}

    for order_id in order_ids:
        doc = await coll.find_one(
            {"order_id": order_id},
            {"unpackedItems.isCase": 1}
        )

        if not doc or not doc.get("unpackedItems"):
            continue

        has_case_true = False
        has_case_false = False

        for item in doc["unpackedItems"]:
            if item.get("isCase") is True:
                has_case_true = True
            elif item.get("isCase") is False:
                has_case_false = True

        # Decide filter type
        if has_case_true and has_case_false:
            filter_type = "MIX"
        elif has_case_true:
            filter_type = "B2B"
        else:
            filter_type = "B2C"

        # Update DB
        # await execute_sql(
        #     update_order_filter(),
        #     connection,
        #     params={
        #         "filter": filter_type,
        #         "pid": picklist_id,
        #         "order_id": order_id
        #     },
        #     raise_error=True
        # )

        # Collect result
        order_filter_map[order_id] = filter_type

    return {
        "success": True,
        "orders": order_filter_map
    }




async def test():
    order_ids = [
      

      "ORD/K0-109/28167-S2",
      "KSK-71980",
      "KSR-1633-S1",
      "KSR-1696",
      "KSR-1759",
      "KSR-1757",
      "KSR-1797",
      "KSR-1822",
      "KSR-1834",
      "KSR-1910",
      "KSR-1953",
      "KSR-1973-S1"

    ]

    result = await get_filter_type_mongo(order_ids)
    print(result)


if __name__ == "__main__":
    asyncio.run(test())


{'success': True, 'orders': {'KSK-105249': 'B2C', 'KSK-105253': 'B2C', 'KSK-105280': 'B2C', 'KSK-104905': 'B2C', 'KSR-4228': 'MIX', 'KSR-4227': 'MIX', 'KSR-4225': 'MIX'}}


#  {'KSR-3848': 'B2B', 'KSR-3722': 'MIX', 'KSR-4228': 'MIX', 'KSR-4227': 'MIX', 'KSR-4225': 'MIX', 'KSR-4221': 'B2C', 'KSR-4211': 'MIX', 'KSR-4208': 'B2B', 'KSR-4178': 'B2C', 'KSR-4202': 'MIX', 'KSR-4197': 'MIX', 'KSR-4184': 'B2B', 'KSR-4183': 'MIX'}} 



#  order_id | filter | picklist_id 
# ----------+--------+-------------
#  KSR-3722 | MIX    |         135
#  KSR-3848 | B2B    |         135
#  KSR-4228 | MIX    |         135
#  KSR-4227 | MIX    |         135
#  KSR-4225 | MIX    |         135
#  KSR-4221 | B2C    |         135
#  KSR-4211 | MIX    |         135
#  KSR-4197 | MIX    |         135
#  KSR-4184 | B2B    |         135
# (9 rows)



 'ORD/K0-109/28167-S2': 'B2C', 'KSK-71980': 'B2C', 'KSR-1633-S1': 'MIX', 'KSR-1696': 'MIX', 'KSR-1759': 'MIX', 'KSR-1757': 'MIX', 'KSR-1797': 'B2C', 'KSR-1822': 'B2C', 'KSR-1834': 'B2C', 'KSR-1910': 'B2B', 'KSR-1953': 'B2B', 'KSR-1973-S1': 'B2B' 


