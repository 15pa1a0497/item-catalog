from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Brand, Base, Bag, User

engine = create_engine('sqlite:///bags.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
User1 = User(name="Sharif", email="sharif.ashu1997@gmail.com")

brand1 = Brand(name="sky Bags")
session.add(brand1)
session.commit()

commodity1 = Bag(name="Brat", description="2 Compartments, Lightweight, Front Stash Pocket, Side Water Bottle Mesh Holder, Padded Handles, Double Reinforced Built-To-Last Straps for Rough Usage.", price="$44.01",
                   material=" 600D Polyester + Ripstop", brand=brand1)

session.add(commodity1)
session.commit()

commodity2 = Bag(name="helix", description="Model Number: BPHELFS1GRN Item Height: 44 Centimeters Item Length: 35 Centimeters Item Width: 22 Centimeters Volume Capacity: 29.5 Liters Item Weight: 470 Grams Material: Polyester Special Features: Back Strap, Expandable, Zip Closure, Back Padding Closure: Zipper Inner Material Polycarbonate Strap: Adjustable Water Resistance: Not Water Resistant",
                   price="$47.13", material=" Polyester", brand=brand1)

session.add(commodity2)
session.commit()

commodity3 = Bag(name="bingo plus", description="If there’s anything that’ll make you look forward to going out, it’s BingoPlus. It's features are such to make sure that every day is bright and organized.",
                    price="$28", material="Nylon, Synthetic,polyster", brand=brand1)

session.add(commodity3)
session.commit()

brand2 = Brand(name="American Tourister")
session.add(brand2)
session.commit()

commodity1 = Bag(name="Disney frozen", description="American Tourister brings you a backpack that is perfect for school or travel. Featuring your favorite Frozen characters, this durable polyester bag is made it last. The multiple pockets organize items of various sizes.",
                   price="$34.78", material="polyster,nylon", brand=brand2)

session.add(commodity1)
session.commit()

commodity2 = Bag(name="keystone", description="600D Shiny Poly & 600D Two tone. Zippers are metal, plastic teeth, and nylon coil.",
                   price="$30", material="nylon,polyster", brand=brand2)

session.add(commodity2)
session.commit()

commodity3 = Bag(name="Moonlight", description="This hardside luggage was made for the traveler who brings whimsy and fun on every journey. This spinner was designed for those who love a dash of fun and with great color choices to match your unique personality. This hardside luggage offers plenty of room for all your needs with its book style opening and compartments on both sides.",
                   price="$169.99", material="synthetic fabric", brand=brand2)

session.add(commodity3)
session.commit()

brand3 = Brand(name="wild craft")
session.add(brand3)
session.commit()

commodity1 = Bag(name="vbiger", description="The backpack is classical style and is made of high quality nylon fabric, durable and living waterproof. It's large and lightweight, with adjustable padding shoulder straps, which greatly reduce the pressure to shoulders. ",
                   price="$23.49", material="nylon fabric", brand=brand3)

session.add(commodity1)
session.commit()

commodity2 = Bag(name="blue angel", description="Be the center of attention all-year-round with this stylish, everyday hi-tech daypack",
                   price="$21.79", material="polyster", brand=brand3)

session.add(commodity2)
session.commit()

commodity3 = Bag(name="fuel", description="Further equipped with side zip secure hydration pockets. Designed with an ultra roomy interior, this bag with its soft-hand feel polyester, was designed with YOU in mind striking all the right notes anywhere & everywhere you go.",
                   price="$97.05", material="polyster fabric", brand=brand3)

session.add(commodity3)
session.commit()

brand4 = Brand(name="Nike")
session.add(brand4)
session.commit()

commodity1 = Bag(name="Hayward Futura ", description="Men's Nike Sportswear Hayward Futura 2.0 Backpack is a new twist on an old favorite with plenty of room for your gear. The durable shell features a new graphic along with additional pockets for extra small-item storage.",
                   price="$45.30", material="polyster", brand=brand4)

session.add(commodity1)
session.commit()

commodity2 = Bag(name="tycoon ", description="The tycoon Tactical BIG Waist & Shoulder Bag comes enhanced with more exterior PALS webbing, added loop field for patches, paracord retention, padded hip support, and 44% more interior compartment & pocket space. The pack rides comfortably on your hips, making it ideal for day hikes or hunting trips. ",
                   price="24.35", material="synthetic", brand=brand4)

session.add(commodity2)
session.commit()

commodity3 = Bag(name="osage", description="Osage River Range Gear Bag Whether you're heading to the range or going on a weekend hunting expedition.",
                   price="18.23", material="nylon", brand=brand4)

session.add(commodity3)
session.commit()

print("added commodity details!")
