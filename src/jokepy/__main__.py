"""Point d'entrée CLI pour le package jokepy."""

import argparse
import sys
from typing import Optional

from .generator import get_all_categories, get_jokes_count, get_random_joke


def main() -> None:
    """Point d'entrée principal du CLI."""
    parser = argparse.ArgumentParser(
        description="Générateur de blagues aléatoires en français",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  jokepy                    # Affiche une blague aléatoire
  jokepy -c sport          # Affiche une blague de sport
  jokepy --list-categories # Liste les catégories disponibles
  jokepy --count           # Affiche le nombre total de blagues
  jokepy --count sport     # Affiche le nombre de blagues de sport
        """,
    )

    parser.add_argument(
        "-c",
        "--category",
        choices=get_all_categories(),
        help="Catégorie de blague",
    )
    parser.add_argument(
        "--list-categories",
        action="store_true",
        help="Affiche les catégories disponibles",
    )
    parser.add_argument(
        "--count",
        nargs="?",
        const="",
        help="Affiche le nombre de blagues (optionnel: par catégorie)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="jokepy 0.1.0",
    )

    args = parser.parse_args()

    try:
        if args.list_categories:
            _show_categories()
        elif args.count is not None:
            _show_count(args.count if args.count else None)
        else:
            _show_joke(args.category)
    except ValueError as e:
        print(f"Erreur: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAu revoir !", file=sys.stderr)
        sys.exit(0)


def _show_categories() -> None:
    """Affiche la liste des catégories disponibles."""
    categories = get_all_categories()
    print("🎭 Catégories disponibles :")
    for cat in sorted(categories):
        count = get_jokes_count(cat)
        print(f"  • {cat} ({count} blague{'s' if count > 1 else ''})")


def _show_count(category: Optional[str] = None) -> None:
    """Affiche le nombre de blagues."""
    if category is None:
        count = get_jokes_count()
        print(f"📊 Total : {count} blagues")
    else:
        count = get_jokes_count(category)
        print(f"📊 Catégorie '{category}' : {count} blague{'s' if count > 1 else ''}")


def _show_joke(category: Optional[str] = None) -> None:
    """Affiche une blague."""
    print("🎭 Blague du jour :")
    joke = get_random_joke(category)
    print(f"\n{joke}\n")

    if category:
        print(f"(Catégorie: {category})")


if __name__ == "__main__":
    main()
