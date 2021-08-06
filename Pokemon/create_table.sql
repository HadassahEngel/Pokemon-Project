USE pokimon;

CREATE TABLE pokemon(
    id INT,
    name VARCHAR(20),
    height INT,
    weight INT,
    PRIMARY KEY (id)
);

CREATE TABLE type(
    id_pokemon INT,
    type VARCHAR(20),
    FOREIGN KEY (id_pokemon) REFERENCES pokemon(id),
    PRIMARY KEY (id_pokemon, type)
);

CREATE TABLE owners(
    name VARCHAR(20),
    town VARCHAR(55),
    PRIMARY KEY (name)
);

CREATE TABLE ownedBy(
    name_owner VARCHAR(20),
    id_pokemon INT,
    FOREIGN KEY (name_owner) REFERENCES owners(name),
    FOREIGN KEY (id_pokemon) REFERENCES pokemon(id),
    PRIMARY KEY (name_owner,id_pokemon)
);
