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
  jokepy -n 3              # Affiche 3 blagues aléatoires
  jokepy -c sport          # Affiche une blague de sport
  jokepy -c sport -n 2     # Affiche 2 blagues de sport
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
        "-n",
        "--number",
        type=int,
        default=1,
        metavar="N",
        help="Nombre de blagues à afficher (défaut: 1)",
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

    # Validation du nombre de blagues
    if args.number < 1:
        print("Erreur: Le nombre de blagues doit être positif.", file=sys.stderr)
        sys.exit(1)
    elif args.number > 50:
        print("Erreur: Le nombre maximum de blagues est 50.", file=sys.stderr)
        sys.exit(1)

    try:
        if args.list_categories:
            _show_categories()
        elif args.count is not None:
            _show_count(args.count if args.count else None)
        else:
            _show_joke(args.category, args.number)
    except ValueError as e:
        print(f"Erreur: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nAu revoir !", file=sys.stderr)
        sys.exit(0)


def _show_categories() -> None:
    """Affiche la liste des catégories disponibles."""
    categories = get_all_categories()
    print("📂 Catégories disponibles :")
    for cat in sorted(categories):
        count = get_jokes_count(cat)
        print(f"  • {cat} ({count} blague{'s' if count > 1 else ''})")


def _show_count(category: Optional[str] = None) -> None:
    """Affiche le nombre de blagues."""
    if category is None:
        count = get_jokes_count()
        print(f"📊 Nombre total de blagues : {count}")
        print(f"🎉 {count} blagues disponibles !")
    else:
        count = get_jokes_count(category)
        print(f"📊 Nombre de blagues dans la catégorie '{category}' : {count}")
        jokes_word = "blague" + ("s" if count > 1 else "")
        available_word = "disponible" + ("s" if count > 1 else "")
        print(f"🎭 {count} {jokes_word} de {category} {available_word} !")


def _show_joke(category: Optional[str] = None, count: int = 1) -> None:
    """Affiche une ou plusieurs blagues."""
    if count == 1:
        print("🎭 Blague du jour :")
        joke = get_random_joke(category)
        print(f"\n{joke}\n")
        if category:
            print(f"(Catégorie: {category})")
    else:
        print(f"🎭 {count} blagues du jour :")
        if category:
            print(f"📂 Catégorie: {category}")
        print()

        for i in range(count):
            joke = get_random_joke(category)
            print(f"{i+1}. {joke}")
            if i < count - 1:  # Ne pas ajouter de ligne vide après la dernière
                print()

        if category:
            print(
                f"\n(Toutes les blagues de la catégorie: {category})"
            )


if __name__ == "__main__":
    main()
