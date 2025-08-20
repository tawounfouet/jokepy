"""Module pour générer des blagues aléatoires."""

import random
from typing import Dict, List, Optional

__all__ = ["get_random_joke", "get_all_categories", "get_jokes_count"]

# Liste principale des blagues
JOKES: List[str] = [
    "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? "
    "Parce que sinon ils tombent dans le bateau !",
    "Quel est le comble pour un électricien ? De ne pas être au courant.",
    "Pourquoi les oiseaux ne prennent-ils pas de médicaments ? "
    "Parce qu'ils ont déjà des ailes.",
    "Que dit une imprimante à une autre ? 'Tu as papier ?'",
    "Pourquoi les maths sont tristes ? Parce qu'elles ont trop de problèmes.",
    "Que dit un escargot quand il croise une limace ? 'Regarde le nudiste !'",
    "Pourquoi les poissons n'aiment pas jouer au tennis ? "
    "Parce qu'ils ont peur du filet.",
    "Comment appelle-t-on un chat tombé dans un pot de peinture le jour de Noël ? "
    "Un chat-mallow !",
    "Que dit un informaticien quand il se noie ? F1 ! F1 !",
    "Pourquoi les développeurs préfèrent-ils le mode sombre ? "
    "Parce que la lumière attire les bugs !",
    "Qu'est-ce qui est jaune et qui attend ? Jonathan !",
    "Comment appelle-t-on un boomerang qui ne revient pas ? Un bâton !",
    "Pourquoi les professeurs d'histoire n'ont jamais froid ? "
    "Parce qu'ils sont entourés de Napoléon !",
    "Que dit un paresseux quand on lui demande de l'aide ? "
    "Je ne peux pas, j'ai tennis !",
    "Comment fait-on pour allumer un barbecue breton ? On utilise des breizh !",
    "Qu'est-ce qu'un cannibale qui mange sa mère ? Un sans-maman !",
    "Pourquoi les bananes ne parlent pas ? Parce qu'elles ont la banane !",
]

# Blagues organisées par catégorie
JOKES_BY_CATEGORY: Dict[str, List[str]] = {
    "sport": [
        "Pourquoi les plongeurs plongent-ils toujours en arrière et jamais en avant ? "
        "Parce que sinon ils tombent dans le bateau !",
        "Pourquoi les poissons n'aiment pas jouer au tennis ? "
        "Parce qu'ils ont peur du filet.",
        "Que dit un paresseux quand on lui demande de l'aide ? "
        "Je ne peux pas, j'ai tennis !",
    ],
    "travail": [
        "Quel est le comble pour un électricien ? De ne pas être au courant.",
        "Que dit une imprimante à une autre ? 'Tu as papier ?'",
        "Que dit un informaticien quand il se noie ? F1 ! F1 !",
        "Pourquoi les développeurs préfèrent-ils le mode sombre ? "
        "Parce que la lumière attire les bugs !",
    ],
    "animaux": [
        "Pourquoi les oiseaux ne prennent-ils pas de médicaments ? "
        "Parce qu'ils ont déjà des ailes.",
        "Que dit un escargot quand il croise une limace ? 'Regarde le nudiste !'",
        "Comment appelle-t-on un chat tombé dans un pot de peinture le jour de Noël ? "
        "Un chat-mallow !",
        "Comment appelle-t-on un boomerang qui ne revient pas ? Un bâton !",
        "Pourquoi les bananes ne parlent pas ? Parce qu'elles ont la banane !",
    ],
    "école": [
        "Pourquoi les maths sont tristes ? Parce qu'elles ont trop de problèmes.",
        "Pourquoi les professeurs d'histoire n'ont jamais froid ? "
        "Parce qu'ils sont entourés de Napoléon !",
    ],
    "humour": [
        "Qu'est-ce qui est jaune et qui attend ? Jonathan !",
        "Comment fait-on pour allumer un barbecue breton ? On utilise des breizh !",
        "Qu'est-ce qu'un cannibale qui mange sa mère ? Un sans-maman !",
    ],
}


def get_random_joke(category: Optional[str] = None) -> str:
    """
    Retourne une blague aléatoire.

    Args:
        category: Catégorie de blague souhaitée. Si None, retourne
                 une blague de n'importe quelle catégorie.

    Returns:
        Une blague sous forme de chaîne de caractères.

    Raises:
        ValueError: Si la catégorie spécifiée n'existe pas.

    Examples:
        >>> joke = get_random_joke()
        >>> isinstance(joke, str)
        True
        >>> joke = get_random_joke("sport")
        >>> isinstance(joke, str)
        True
    """
    if category is None:
        return random.choice(JOKES)

    if category not in JOKES_BY_CATEGORY:
        available = ", ".join(JOKES_BY_CATEGORY.keys())
        raise ValueError(
            f"Catégorie '{category}' inconnue. " f"Catégories disponibles: {available}"
        )

    return random.choice(JOKES_BY_CATEGORY[category])


def get_all_categories() -> List[str]:
    """
    Retourne la liste de toutes les catégories disponibles.

    Returns:
        Liste des noms de catégories.

    Examples:
        >>> categories = get_all_categories()
        >>> "sport" in categories
        True
    """
    return list(JOKES_BY_CATEGORY.keys())


def get_jokes_count(category: Optional[str] = None) -> int:
    """
    Retourne le nombre de blagues disponibles.

    Args:
        category: Catégorie spécifique ou None pour le total.

    Returns:
        Nombre de blagues.

    Raises:
        ValueError: Si la catégorie spécifiée n'existe pas.

    Examples:
        >>> count = get_jokes_count()
        >>> count > 0
        True
    """
    if category is None:
        return len(JOKES)

    if category not in JOKES_BY_CATEGORY:
        raise ValueError(f"Catégorie '{category}' inconnue.")

    return len(JOKES_BY_CATEGORY[category])


# Test if __name__ == "__main__":
if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print("Tous les tests ont réussi !")
    print("Utilisez `get_random_joke()` pour obtenir une blague aléatoire.")
    print("Utilisez `get_all_categories()` pour voir les catégories disponibles.")
    print("Utilisez `get_jokes_count()` pour connaître le nombre de blagues.")
