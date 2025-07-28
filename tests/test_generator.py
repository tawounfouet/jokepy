"""Tests pour le module generator."""

import pytest

from jokepy.generator import (
    JOKES,
    JOKES_BY_CATEGORY,
    get_all_categories,
    get_jokes_count,
    get_random_joke,
)


class TestGetRandomJoke:
    """Tests pour la fonction get_random_joke."""

    def test_returns_string(self):
        """Test que get_random_joke retourne une chaîne."""
        joke = get_random_joke()
        assert isinstance(joke, str)

    def test_returns_valid_joke(self):
        """Test que la blague retournée fait partie de la liste JOKES."""
        joke = get_random_joke()
        assert joke in JOKES

    def test_returns_string_with_category(self):
        """Test que get_random_joke retourne une chaîne avec catégorie."""
        joke = get_random_joke("sport")
        assert isinstance(joke, str)

    def test_returns_valid_joke_with_category(self):
        """Test que la blague retournée fait partie de la catégorie."""
        joke = get_random_joke("sport")
        assert joke in JOKES_BY_CATEGORY["sport"]

    def test_invalid_category_raises_error(self):
        """Test qu'une catégorie invalide lève une ValueError."""
        with pytest.raises(ValueError, match="Catégorie 'inexistante' inconnue"):
            get_random_joke("inexistante")

    def test_random_behavior(self):
        """Test que la fonction retourne différentes blagues (probabiliste)."""
        # Ce test pourrait échouer par malchance, mais très peu probable
        jokes = {get_random_joke() for _ in range(20)}
        assert len(jokes) > 1  # On s'attend à avoir au moins 2 blagues différentes


class TestGetAllCategories:
    """Tests pour la fonction get_all_categories."""

    def test_returns_list(self):
        """Test que get_all_categories retourne une liste."""
        categories = get_all_categories()
        assert isinstance(categories, list)

    def test_contains_expected_categories(self):
        """Test que les catégories attendues sont présentes."""
        categories = get_all_categories()
        expected = ["sport", "travail", "animaux", "école"]
        for category in expected:
            assert category in categories

    def test_all_elements_are_strings(self):
        """Test que tous les éléments sont des chaînes."""
        categories = get_all_categories()
        for category in categories:
            assert isinstance(category, str)


class TestGetJokesCount:
    """Tests pour la fonction get_jokes_count."""

    def test_returns_int(self):
        """Test que get_jokes_count retourne un entier."""
        count = get_jokes_count()
        assert isinstance(count, int)

    def test_returns_positive_count(self):
        """Test que le nombre de blagues est positif."""
        count = get_jokes_count()
        assert count > 0

    def test_returns_correct_total_count(self):
        """Test que le nombre total correspond à la longueur de JOKES."""
        count = get_jokes_count()
        assert count == len(JOKES)

    def test_returns_correct_category_count(self):
        """Test que le nombre par catégorie est correct."""
        count_sport = get_jokes_count("sport")
        assert count_sport == len(JOKES_BY_CATEGORY["sport"])

    def test_invalid_category_raises_error(self):
        """Test qu'une catégorie invalide lève une ValueError."""
        with pytest.raises(ValueError, match="Catégorie 'inexistante' inconnue"):
            get_jokes_count("inexistante")


class TestDataConsistency:
    """Tests pour vérifier la cohérence des données."""

    def test_jokes_list_not_empty(self):
        """Test que la liste JOKES n'est pas vide."""
        assert len(JOKES) > 0

    def test_all_jokes_are_strings(self):
        """Test que toutes les blagues sont des chaînes non vides."""
        for joke in JOKES:
            assert isinstance(joke, str)
            assert len(joke.strip()) > 0

    def test_categories_not_empty(self):
        """Test que chaque catégorie contient au moins une blague."""
        for category, jokes in JOKES_BY_CATEGORY.items():
            assert len(jokes) > 0
            assert isinstance(category, str)

    def test_category_jokes_are_in_main_list(self):
        """Test que toutes les blagues des catégories sont dans JOKES."""
        for category, jokes in JOKES_BY_CATEGORY.items():
            for joke in jokes:
                assert joke in JOKES

    def test_no_duplicate_jokes_in_main_list(self):
        """Test qu'il n'y a pas de doublons dans JOKES."""
        assert len(JOKES) == len(set(JOKES))
