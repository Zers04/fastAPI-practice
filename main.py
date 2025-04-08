from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI(
    title="Veterinaria Margarita 😺",
    description="API para gestionar animales en la veterinaria Margarita",
    version="1.0.0",
)

models.Base.metadata.create_all(bind=engine)

class animalBase(BaseModel):
    id: int
    especie: str
    raza: str
    nombre: str
    edad: int
    peso: float

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_depndency = Annotated[Session, Depends(get_db)]

@app.post("/animales/")
async def create_animal(animal: animalBase, db: db_depndency):

    # Validate the input data
    if not animal.especie or not animal.raza or not animal.nombre or not animal.edad or not animal.peso:
        raise HTTPException(status_code=400, detail="Invalid input data")
    
    # Check if the species is valid
    species = [e.value for e in models.EspecieEnum]
    if animal.especie not in species:
        raise HTTPException(status_code=400, detail="Invalid species, must be 'perro' or 'gato'")
    
    # Check if the breed is valid
    breeds = [e.value for e in models.RazaEnum]
    if animal.raza not in breeds:
        raise HTTPException(status_code=400, detail="Invalid breed, must be 'criollo' or 'fino'")

    # Check if the age and weight are valid
    if animal.edad <= 0:
        raise HTTPException(status_code=400, detail="Invalid age")
    
    if animal.peso <= 0:
        raise HTTPException(status_code=400, detail="Invalid weight")
    
    # Check if the animal already exists in the database same name, species and breed
    existing_animal = db.query(models.Animals).filter(models.Animals.nombre == animal.nombre, models.Animals.especie == animal.especie, models.Animals.raza == animal.raza).first()
    if existing_animal:
        raise HTTPException(status_code=400, detail="Animal already exists")
    

    # Create a new animal instance
    db_animal = models.Animals(especie=animal.especie, raza=animal.raza, nombre=animal.nombre, edad=animal.edad, peso=animal.peso)
    
    # Add the new animal to the database
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal

@app.get("/animales/", response_model=List[animalBase])
async def read_animals(db: db_depndency):

    # Get all animals from the database
    animals = db.query(models.Animals).all()

    # Check if there are any animals in the database
    if not animals:
        return {"message": "No animals found"}

    return animals


@app.get("/animales/{animal_id}", response_model=animalBase)
async def read_animal(animal_id: int, db: db_depndency):
    # Get a specific animal by ID from the database
    animal = db.query(models.Animals).filter(models.Animals.id == animal_id).first()

    # Check if the animal exists in the database
    if animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    
    return animal


@app.put("/animales/{animal_id}", response_model=animalBase)
async def update_animal(animal_id: int, animal: animalBase, db: db_depndency):
    
    # Check if the species is valid
    species = [e.value for e in models.EspecieEnum]
    if animal.especie not in species:
        raise HTTPException(status_code=400, detail="Invalid species, must be 'perro' or 'gato'")
    
    # Check if the breed is valid
    breeds = [e.value for e in models.RazaEnum]
    if animal.raza not in breeds:
        raise HTTPException(status_code=400, detail="Invalid breed, must be 'criollo' or 'fino'")
    
    # Check if the age and weight are valid
    if animal.edad <= 0:
        raise HTTPException(status_code=400, detail="Invalid age")
    
    if animal.peso <= 0:
        raise HTTPException(status_code=400, detail="Invalid weight")

    # Check if the animal exists in the database
    db_animal = db.query(models.Animals).filter(models.Animals.id == animal_id).first()

    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    
    # Update the animal's attributes
    db_animal.especie = animal.especie
    db_animal.raza = animal.raza
    db_animal.nombre = animal.nombre
    db_animal.edad = animal.edad
    db_animal.peso = animal.peso

    # Add the updated animal to the database
    db.commit()
    db.refresh(db_animal)
    return db_animal

@app.delete("/animales/{animal_id}")
async def delete_animal(animal_id: int, db: db_depndency):
    db_animal = db.query(models.Animals).filter(models.Animals.id == animal_id).first()
    if db_animal is None:
        raise HTTPException(status_code=404, detail="Animal not found")
    db.delete(db_animal)
    db.commit()
    return {"detail": "Animal deleted"}
