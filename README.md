# Pyrene 🏔️

> ⚠️ **This project is under development** ⚠️

**Pyrene** is an application that obtains data from the avalanche bulletins of the Pyrenees.

## 📖️ The Legend

Legend has it that a long time ago Geryon, the deformed 3-headed creature, defeated King Tubal.

Pyrene, in love with Hercules, knowing that the monster would come after her, flees to the forests of the plains,
home of gods, demigods and men, to hide from the horrible 3-headed monster.

Geryon in love and rejected by Pyrene, he knew that he had to kill the princess to be able to take full control as the new king of Hispania.
He chases her, reaching the border with the neighboring country.

Not finding it, he decides to burn all that vast territory. Thinking that the princess would die in the flames.
The fire spread across one of the most beautiful mountain ranges in Spain that today is known as the Pyrenees.

Hercules, the great warrior and demigod who fought against the enemies of Iberia, could not save the beautiful and
beloved Princess Pyrene. Sad and heartbroken, with his heart broken, he covered her body with an ash mantle. Furthermore,
on the body of the beautiful princess, he piled up large stones in the shape of a mausoleum.

## 🌍️ Supported Regions

At the moment the following regions are supported:

- Val d'Aran - [Lauegi](https://lauegi.report)
- Catalonia - [ICGC](https://bpa.icgc.cat)

## Run

### 🐳️ Docker

1. Build docker image:
    ```bash
    docker build -t pyrene:latest
    ```

2. Run Pyrene:
    ```bash
    docker run \
      -e MY_ENV=my-value \
      --rm \
      --name pyrene \
      pyrene:latest
    ```

### 💻️ Virtualenv (Pipfile)

#### Requirements

- [Python +3.12](https://www.python.org)
- [Pipenv](https://pipenv.pypa.io)

1. Run Pyrene:
   ```bash
   pipenv run pyrene
   ```

### 🧪️ Tests

> ℹ️ Tests are not available yet for this project.

This project uses [Pytest](https://docs.pytest.org).

1. Run tests:
   ```bash
   pipenv run test
   ```

## 💪️ Contributing

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

Follow this [guideline](./.github/CONTRIBUTING) to submit a change.

## 🏛️ License

This project is licensed under the terms of the [GNU Affero General Public License](./LICENSE).

## 👨‍💻️ Contributors

- **Nil Torrano**: [ntorrano@atesmaps.org](mailto:ntorrano@atesmaps.org)
- **Atesmaps Team**: [info@atesmaps.org](mailto:info@atesmaps.org)
