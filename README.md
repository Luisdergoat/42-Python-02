## This project has been created as part of the 42 curriculum by lunsold
---

# 42-Python-02 🌱

## 📋 Projektübersicht

## Dieses Repository enthält die Lösungen für das Python Modul 02 der 42 Schule.

![42 Badge](https://img.shields.io/badge/42-Project-blue)
![Language](https://img.shields.io/badge/Language-python-orange)


Python Projekt für fortgeschrittenes Error Handling und Datenstrukturen.

## 📋 Projekt

**Garden Management System** - Ein intelligentes Gartenverwaltungssystem mit umfassendem Error Handling. 

## ✨ Features

- **Custom Exceptions**: Eigene Error-Typen für gartenspezifische Probleme
- **Linked List Implementation**: Pflanzenverwaltung mit verketteten Listen
- **Error Handling**: Try/Except/Finally Blöcke mit Cleanup
- **Error Recovery**: System läuft weiter trotz Fehlern
- **Resource Management**: Automatische Freigabe von Ressourcen

## 🚀 Verwendung

```python
from ft_garden_management import GardenManager

# Garden erstellen
garden = GardenManager(max_plants=10)

# Pflanzen hinzufügen
garden.add_plant_to_list("Tomato", water_requirement=3)
garden.add_plant_to_list("Cucumber", water_requirement=2)

# Pflanzen gießen
garden.water_plant("Tomato", amount=3)

# Status prüfen
garden.check_all_plants()
```

## 🛠️ Error Types

- `EmptyNameError` - Leerer Pflanzenname
- `DuplicatePlantError` - Pflanze existiert bereits  
- `GardenFullError` - Garten hat maximale Kapazität erreicht
- `PlantNotFoundError` - Pflanze nicht gefunden
- `InvalidWaterAmountError` - Ungültige Wassermenge
- `DeadPlantError` - Pflanze ist tot

## 📦 Struktur

```
ex5/
└── ft_garden_management. py    # Hauptprogramm mit GardenManager
```

## ✅ Tests

```bash
python ft_garden_management. py
```

## 👤 Autor

lunsold - 42 School Project