## This project has been created as part of the 42 curriculum by lunsold
---

# 42-Python-02 🌱

## 📋 Projektübersicht

## Dieses Repository enthält die Lösungen für das Python Modul 02 der 42 Schule.

![42 Badge](https://img.shields.io/badge/42-Project-blue)
![Language](https://img.shields.io/badge/Language-python-orange)

Python Projekt für fortgeschrittenes Error Handling und Datenstrukturen.

## 📂 Übungen

### ex0: First Exception
**Temperature Checker** - Erste Schritte mit Try/Except Blöcken
- Eingabevalidierung mit Exception Handling
- ValueError Handling für ungültige Eingaben
- Temperaturprüfung für Pflanzenwachstum (0°C - 40°C)

### ex1: Different Error Types
**Multiple Error Types** - Umgang mit verschiedenen Error-Typen
- `ValueError` - Ungültige Zahleneingaben
- `ZeroDivisionError` - Division durch Null
- `FileNotFoundError` - Fehlende Dateien
- `KeyError` - Fehlende Dictionary-Keys

### ex2: Custom Errors
**Custom Exception Classes** - Eigene Error-Klassen erstellen
- `GardenError` - Basis-Fehlerklasse
- `WateringError` - Fehler bei Bewässerung
- `PlantError` - Pflanzenbezogene Fehler
- Vererbung von Exception-Klassen

### ex3: Finally Block
**Cleanup with Finally** - Ressourcen-Management mit Finally
- Linked List Implementation für Pflanzenverwaltung
- Finally-Blöcke für garantierte Cleanup-Operationen
- Wasserstatus-Tracking pro Pflanze

### ex4: Raise Errors
**Raising Exceptions** - Eigene Exceptions werfen
- Validierung von Pflanzendaten
- Raise von ValueError bei ungültigen Werten
- Gesundheitsprüfung:  Wasserlevel (2-10) und Sonnenstunden (2-12)

### ex5: Garden Management System
**Complete Error Handling System** - Umfassendes Gartenverwaltungssystem
- Custom Exception Hierarchy
- Linked List für Pflanzenverwaltung
- Umfassendes Error Handling und Recovery

## ✨ Features (ex5)

- **Custom Exceptions**:  Eigene Error-Typen für gartenspezifische Probleme
- **Linked List Implementation**: Pflanzenverwaltung mit verketteten Listen
- **Error Handling**: Try/Except/Finally Blöcke mit Cleanup
- **Error Recovery**: System läuft weiter trotz Fehlern
- **Resource Management**: Automatische Freigabe von Ressourcen
- **Operation Logging**: Nachverfolgung aller Operationen

## 🛠️ Error Types (ex5)

- `EmptyNameError` - Leerer Pflanzenname
- `DuplicatePlantError` - Pflanze existiert bereits  
- `GardenFullError` - Garten hat maximale Kapazität erreicht
- `PlantNotFoundError` - Pflanze nicht gefunden
- `InvalidWaterAmountError` - Ungültige Wassermenge
- `DeadPlantError` - Pflanze ist tot

## 🚀 Verwendung

```python
from ft_garden_management import GardenManager

# Garden erstellen
garden = GardenManager(max_plants=10)

# Pflanzen hinzufügen
garden.add_plant_to_list("Tomato", water_requirement=3)
garden.add_plant_to_list("Cucumber", water_requirement=2)

# Pflanzen gießen
garden.water_plant(amount=3)

# Status prüfen
garden.check_all_plants()
```

## 📦 Struktur

```
42-Python-02/
├── ex0/
│   └── ft_first_exception.py       # Basis Exception Handling
├── ex1/
│   └── ft_different_errors.py      # Verschiedene Error-Typen
├── ex2/
│   └── ft_custom_errors.py         # Custom Exception Classes
├── ex3/
│   └── ft_finally_block.py         # Finally Blocks & Cleanup
├── ex4/
│   └── ft_raise_errors.py          # Raising Exceptions
└── ex5/
    └── ft_garden_management.py     # Vollständiges System
```

## ✅ Tests

Jede Übung kann einzeln getestet werden:

```bash
# Test ex0 - First Exception
python ex0/ft_first_exception. py

# Test ex1 - Different Errors
python ex1/ft_different_errors.py

# Test ex2 - Custom Errors
python ex2/ft_custom_errors.py

# Test ex3 - Finally Block
python ex3/ft_finally_block.py

# Test ex4 - Raise Errors
python ex4/ft_raise_errors.py

# Test ex5 - Garden Management
python ex5/ft_garden_management.py
```

## 🎯 Lernziele

- ✅ Exception Handling mit try/except/finally
- ✅ Verschiedene Built-in Error Types verstehen
- ✅ Custom Exception Classes erstellen
- ✅ Error Recovery und Cleanup
- ✅ Linked Lists in Python implementieren
- ✅ Resource Management
- ✅ Defensive Programming

## 👤 Autor

**lunsold** - 42 School Project  
Repository:  [Luisdergoat/42-Python-02]
(https://github.com/Luisdergoat/42-Python-02)