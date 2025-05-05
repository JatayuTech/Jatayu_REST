from sqlalchemy import String, and_, or_, select, text
from models import books,client,transport 
from database import database
from schemas import BookIn, clientIn

async def create_book(book: BookIn):
    query = books.insert().values(
        title=book.title,
        author=book.author,
        year=book.year
    )
    await database.execute(query)

async def getData(year: int,y:int):
    query = select(books).where(
        or_(
            books.c.year == year,
            books.c.year == y
        )
    )
    return await database.fetch_all(query)


async def clientSave(cl:clientIn):
    query=client.insert().values(
        source=cl.source,
        destination=cl.destination,
        noOfDdays=cl.noOfDdays,
        TravelPreference=cl.TravelPreference,
        AccPreference=cl.AccPreference,
        FoodSuggestion=cl.FoodSuggestion,
        Sightseeing=cl.Sightseeing
    )
    await database.execute(query)


async def getTData(c:clientIn):
  
  query = select(transport).where(
    and_(
        transport.c.Tsrc == c.source,
        transport.c.Tdes == c.destination,
        transport.c.TypeofRoute == c.TravelPreference + "-Route"
    )
)
  return await database.fetch_all(query)

async def getclientData(src: int):
    qu = select(client).where(client.c.id == src)
    result = await database.fetch_all(qu)
    
    transport_data = []
    for record in result:
        query = select(transport).where(
            and_(
                transport.c.Tsrc == record['source'],
                transport.c.Tdes == record['destination'],
                transport.c.TypeofRoute == record['TravelPreference'] + "-Route"
            )
        )
        transport_data.append(await database.fetch_all(query))

    for record in result:
        query = select(transport).where(
            and_(
                transport.c.Tsrc == record['destination'],
                transport.c.Tdes == record['source'],
                transport.c.TypeofRoute == record['TravelPreference'] + "-EnRoute"
            )
        )
        transport_data.append(await database.fetch_all(query))
    
    return transport_data



