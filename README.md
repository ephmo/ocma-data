# OCMA-Data

![Stage](https://img.shields.io/badge/stage-alpha-orange)
![Build](https://img.shields.io/github/actions/workflow/status/ephmo/ocma-data/deploy.yml)
![Coverage](https://img.shields.io/badge/coverage-68%25-yellow)
![License](https://img.shields.io/github/license/ephmo/ocma-data)

---

## Overview

**OCMA-Data** is a comprehensive and structured **Orthodox Christian liturgical calendar dataset**. It provides machine-readable **JSON files for each liturgical year**, supporting both the **Old Calendar (Julian)** and the **New Calendar (Revised Julian)** for the years **1924–2099**.

This repository serves as the canonical data source for the **[OCMA](https://github.com/ephmo/ocma)** application, while remaining **framework-agnostic** and reusable for a wide range of applications and research projects.

---

## Key Features

### 📅 Calendar Coverage

- Fixed and movable feast cycles
- Complete Paschal cycle for each supported year
- Old Calendar (Julian) and New Calendar (Revised Julian) alignment

### 🕯️ Liturgical Content

- **Feasts**: Great, Major, Minor and Lesser feasts
- **Saints**: Common Saints and additional local Saints
- **Fasting Rules**: Fasting seasons and daily fasting levels
- **Lectionary**:
  - Tone of the week
  - Sunday Matins Gospel, Epistle and Gospel

### 🌕 Astronomical Data

- Pascha date per year
- Primary lunar phases relevant to the liturgical calendar

---

## Multilingual Support

OCMA-Data is designed to be **fully translation-friendly**.

- Supported languages:
  - English
  - Greek
  - Romanian
  - Russian

Each language is stored in **separate JSON files**, ensuring a strict separation between:

- **Liturgical logic and calendar calculations**
- **Human-readable language content**

This approach allows new languages to be added easily without modifying the core calendar data.

---

## Data Structure

OCMA-Data follows a **year-based, language-separated JSON structure**:

- **One JSON file per year**, containing all liturgical days and data for that year
- **One JSON file per language**, holding translated textual content
- **One unified Paschalion JSON file**, covering Pascha dates for **all supported years**

This structure provides:

- Predictable file organization
- Efficient data loading for applications
- Clear separation of concerns between calendar logic and translations

The dataset is optimized for **clarity, maintainability, and long-term extensibility**.

---

## Use Cases

OCMA-Data is suitable for:

- **Developers** building Orthodox calendar applications
- **Researchers** analyzing Orthodox liturgical cycles and calendar systems
- **Church organizations** requiring structured liturgical data
- **Faithful** seeking programmatic access to daily liturgical information

---

## Contributing

Contributions are welcome and encouraged.

You can help by:

- Adding new language translations
- Improving existing translations
- Correcting or enriching liturgical data
- Enhancing documentation

Please submit a pull request or open an issue to discuss proposed changes.

---

## Reporting Issues

If you encounter bugs, data inconsistencies, or have suggestions for improvement, please open an issue on the GitHub tracker:

👉 https://github.com/ephmo/ocma-data/issues

Your feedback helps improve the quality and reliability of the dataset.

---

## License

OCMA-Data is released under the **MIT License**.

See the [LICENSE](LICENSE) file for full details.
