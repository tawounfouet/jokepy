Installation
============

🔧 Prérequis
------------

* Python 3.8 ou supérieur
* pip (généralement inclus avec Python)

💾 Installation depuis PyPI
---------------------------

La méthode recommandée pour installer jokepy :

.. code-block:: bash

   pip install jokepy

🔄 Installation depuis les sources
----------------------------------

Pour obtenir la version de développement :

.. code-block:: bash

   # Cloner le repository
   git clone https://github.com/yourusername/jokepy.git
   cd jokepy
   
   # Installer en mode développement
   pip install -e .

🏗️ Installation pour le développement
-------------------------------------

Si vous souhaitez contribuer au projet :

.. code-block:: bash

   # Cloner le repository
   git clone https://github.com/yourusername/jokepy.git
   cd jokepy
   
   # Créer un environnement virtuel
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   # venv\Scripts\activate   # Sur Windows
   
   # Installer avec les dépendances de développement
   pip install -e ".[dev,docs]"
   
   # Configurer pre-commit (optionnel)
   pre-commit install

✅ Vérification de l'installation
---------------------------------

Pour vérifier que l'installation s'est bien déroulée :

.. code-block:: bash

   # Tester le CLI
   jokepy --help
   
   # Tester en Python
   python -c "from jokepy import get_random_joke; print(get_random_joke())"

🐛 Résolution de problèmes
--------------------------

Problèmes courants et solutions :

**Erreur "command not found: jokepy"**

Assurez-vous que le répertoire des scripts Python est dans votre PATH, ou utilisez :

.. code-block:: bash

   python -m jokepy

**Erreur d'importation**

Vérifiez que vous êtes dans le bon environnement virtuel :

.. code-block:: bash

   which python
   pip list | grep jokepy
