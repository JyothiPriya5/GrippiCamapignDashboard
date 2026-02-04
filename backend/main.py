from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database setup
DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

# Campaign Model
class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String)
    clicks = Column(Integer)
    cost = Column(Float)
    impressions = Column(Integer)

# Create table
Base.metadata.create_all(bind=engine)

# App
app = FastAPI()

# Allow frontend access (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API endpoint
@app.get("/campaigns")
def get_campaigns():
    db = SessionLocal()
    campaigns = db.query(Campaign).all()
    db.close()
    return campaigns


# Insert sample data (run once)
@app.on_event("startup")
def insert_data():
    db = SessionLocal()

    if db.query(Campaign).count() == 0:
        sample = [
            Campaign(name="Summer Sale", status="Active", clicks=150, cost=45.99, impressions=1000),
            Campaign(name="Black Friday", status="Paused", clicks=320, cost=89.50, impressions=2500),
            Campaign(name="Winter Deals", status="Active", clicks=210, cost=60.25, impressions=1800),
            Campaign(name="New Launch", status="Active", clicks=400, cost=120.75, impressions=5000),
            Campaign(name="Clearance", status="Paused", clicks=90, cost=20.00, impressions=600),
            Campaign(name="Festive Offer", status="Active", clicks=275, cost=70.10, impressions=2200),
            Campaign(name="Flash Sale", status="Paused", clicks=180, cost=55.00, impressions=1500),
            Campaign(name="Referral Bonus", status="Active", clicks=350, cost=95.60, impressions=3200),
            Campaign(name="Weekend Deal", status="Paused", clicks=140, cost=38.75, impressions=900),
            Campaign(name="Mega Offer", status="Active", clicks=500, cost=150.00, impressions=6000),
        ]

        db.add_all(sample)
        db.commit()

    db.close()
