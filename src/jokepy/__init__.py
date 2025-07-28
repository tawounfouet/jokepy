"""Package jokepy pour générer des blagues aléatoires."""

__version__ = "0.1.0"

from .generator import get_all_categories, get_jokes_count, get_random_joke

__all__ = ["get_random_joke", "get_all_categories", "get_jokes_count"]
