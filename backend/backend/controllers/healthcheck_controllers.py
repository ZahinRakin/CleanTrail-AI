from backend.models.user_model import User
from backend.models.admin_model import Admin
from backend.models.customer_model import Customer
from backend.models.email_model import Email
from backend.models.news_model import News
from backend.models.notification_model import Notification
from backend.models.product_model import Product
from backend.models.store_model import Store
from backend.models.store_owner_model import StoreOwner
from datetime import datetime, timezone, timedelta
import os
from jose import jwt # type: ignore


async def check_all():
    # user
    user = await User(
        fname="demo",
        lname="demos",
        email="demo@gmail.com",
        username="demo username",
        password="Rakin123*"
    ).insert()
    
    payload = {
        "id": str(user.id),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }
    refresh_token = jwt.encode(claims=payload, key=os.getenv("REFRESH_TOKEN_SECRET"), algorithm="HS256")
    # user.update_one({"id": user.id}, {"$set": {
    #     "refresh_token": refresh_token
    # }})
    user.refresh_token = refresh_token
    await user.save()

    # admin
    admin = await Admin(user=user).insert()

    # customer
    customer = await Customer(user=user).insert()

    # email
    email = await Email(
        sender="zahinabdullahrakin@gmail.com",
        receiver="zahinabdullahrakin@gmail.com",
        subject="demo",
        body="demo",
    ).insert()

    # product
    product = await Product(
        name="product 1",
        description="this is pure joy of a product",
    ).insert()

    # news
    news = await News(
        product=product,
        title="this is the launch of the exciting ponds",
        description="Hello world. How are you? Today I am thrilled to announce that the new ponds have been launched. You can purchase it in this link"
    ).insert()

    # notification
    notification = await Notification(
        sender=user,
        receiver=user,
        title="notification title",
        description="Nothing on my mind to say"
    ).insert()

    # store
    store = await Store(
        name="zarbazar",
        products=[product]
    ).insert()

    # store owner (FIXED: should reference Store, not Product)
    store_owner = await StoreOwner(
        stores=[store]  # ✅ FIXED: should reference stores, not products
    ).insert()

    return {
        "message": "user created."
    }
