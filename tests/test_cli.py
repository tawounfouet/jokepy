"""Tests pour le module CLI (__main__)."""

import io
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

import pytest

from jokepy.__main__ import _show_categories, _show_count, _show_joke, main


class TestShowJoke:
    """Tests pour la fonction _show_joke."""

    def test_show_joke_no_category(self):
        """Test l'affichage d'une blague sans catégorie."""
        output = io.StringIO()
        with redirect_stdout(output):
            _show_joke()
        result = output.getvalue()
        assert "🎭 Blague du jour :" in result
        assert result.count("\n") >= 3  # Au moins titre + blague + ligne vide

    def test_show_joke_with_category(self):
        """Test l'affichage d'une blague avec catégorie."""
        output = io.StringIO()
        with redirect_stdout(output):
            _show_joke("sport")
        result = output.getvalue()
        assert "🎭 Blague du jour :" in result
        assert "(Catégorie: sport)" in result

    def test_show_joke_invalid_category_raises_error(self):
        """Test qu'une catégorie invalide lève une ValueError."""
        with pytest.raises(ValueError):
            _show_joke("inexistante")

    def test_show_joke_multiple(self):
        """Test l'affichage de plusieurs blagues."""
        output = io.StringIO()
        with redirect_stdout(output):
            _show_joke(count=3)
        result = output.getvalue()
        assert "🎭 3 blagues du jour :" in result
        assert "1." in result
        assert "2." in result
        assert "3." in result

    def test_show_joke_multiple_with_category(self):
        """Test l'affichage de plusieurs blagues avec catégorie."""
        output = io.StringIO()
        with redirect_stdout(output):
            _show_joke("sport", 2)
        result = output.getvalue()
        assert "🎭 2 blagues du jour :" in result
        assert "📂 Catégorie: sport" in result
        assert "(Toutes les blagues de la catégorie: sport)" in result


class TestShowCategories:
    """Tests pour la fonction _show_categories."""

    def test_show_categories_output(self):
        """Test l'affichage des catégories."""
        output = io.StringIO()
        with redirect_stdout(output):
            _show_categories()
        result = output.getvalue()
        assert "📂 Catégories disponibles :" in result
        assert "sport" in result
        assert "travail" in result
        assert "animaux" in result
        assert "école" in result
        assert "humour" in result


class TestShowCount:
    """Tests pour la fonction _show_count."""

    def test_show_count_total(self):
        """Test l'affichage du nombre total de blagues."""
        output = io.StringIO()
        with redirect_stdout(output):
            _show_count()
        result = output.getvalue()
        assert "📊 Nombre total de blagues :" in result
        assert result.strip().endswith("blagues disponibles !")

    def test_show_count_by_category(self):
        """Test l'affichage du nombre de blagues par catégorie."""
        output = io.StringIO()
        with redirect_stdout(output):
            _show_count("sport")
        result = output.getvalue()
        assert "📊 Nombre de blagues dans la catégorie 'sport' :" in result

    def test_show_count_invalid_category_raises_error(self):
        """Test qu'une catégorie invalide lève une ValueError."""
        with pytest.raises(ValueError):
            _show_count("inexistante")


class TestMain:
    """Tests pour la fonction main."""

    def test_main_no_args(self):
        """Test l'exécution sans arguments (blague aléatoire)."""
        with patch("sys.argv", ["jokepy"]):
            output = io.StringIO()
            with redirect_stdout(output):
                main()
            result = output.getvalue()
            assert "🎭 Blague du jour :" in result

    def test_main_list_categories(self):
        """Test l'option --list-categories."""
        with patch("sys.argv", ["jokepy", "--list-categories"]):
            output = io.StringIO()
            with redirect_stdout(output):
                main()
            result = output.getvalue()
            assert "📂 Catégories disponibles :" in result

    def test_main_count_total(self):
        """Test l'option --count sans catégorie."""
        with patch("sys.argv", ["jokepy", "--count"]):
            output = io.StringIO()
            with redirect_stdout(output):
                main()
            result = output.getvalue()
            assert "📊 Nombre total de blagues :" in result

    def test_main_count_category(self):
        """Test l'option --count avec catégorie."""
        with patch("sys.argv", ["jokepy", "--count", "sport"]):
            output = io.StringIO()
            with redirect_stdout(output):
                main()
            result = output.getvalue()
            assert "📊 Nombre de blagues dans la catégorie 'sport' :" in result

    def test_main_category(self):
        """Test l'option -c/--category."""
        with patch("sys.argv", ["jokepy", "-c", "sport"]):
            output = io.StringIO()
            with redirect_stdout(output):
                main()
            result = output.getvalue()
            assert "🎭 Blague du jour :" in result
            assert "(Catégorie: sport)" in result

    def test_main_invalid_category_exits_with_error(self):
        """Test qu'une catégorie invalide fait sortir le programme avec une erreur."""
        with patch("sys.argv", ["jokepy", "-c", "inexistante"]):
            error_output = io.StringIO()
            with redirect_stderr(error_output):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                # argparse exits with code 2 for invalid arguments
                assert exc_info.value.code == 2
            error_result = error_output.getvalue()
            assert "invalid choice" in error_result.lower()

    def test_main_keyboard_interrupt_graceful_exit(self):
        """Test que Ctrl+C fait sortir proprement le programme."""
        with patch("sys.argv", ["jokepy"]):
            with patch("jokepy.__main__._show_joke", side_effect=KeyboardInterrupt):
                error_output = io.StringIO()
                with redirect_stderr(error_output):
                    with pytest.raises(SystemExit) as exc_info:
                        main()
                    assert exc_info.value.code == 0
                error_result = error_output.getvalue()
                assert "Au revoir !" in error_result

    def test_main_help_option(self):
        """Test l'option --help."""
        with patch("sys.argv", ["jokepy", "--help"]):
            with pytest.raises(SystemExit) as exc_info:
                with redirect_stdout(io.StringIO()):
                    main()
            # L'aide doit sortir avec le code 0
            assert exc_info.value.code == 0

    def test_main_multiple_jokes(self):
        """Test l'option -n/--number pour plusieurs blagues."""
        with patch("sys.argv", ["jokepy", "-n", "3"]):
            output = io.StringIO()
            with redirect_stdout(output):
                main()
            result = output.getvalue()
            assert "🎭 3 blagues du jour :" in result

    def test_main_negative_number_exits_with_error(self):
        """Test qu'un nombre négatif fait sortir le programme avec une erreur."""
        with patch("sys.argv", ["jokepy", "-n", "-1"]):
            error_output = io.StringIO()
            with redirect_stderr(error_output):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                assert exc_info.value.code == 1
            error_result = error_output.getvalue()
            assert "Le nombre de blagues doit être positif" in error_result

    def test_main_too_many_jokes_exits_with_error(self):
        """Test qu'un nombre trop élevé fait sortir le programme avec une erreur."""
        with patch("sys.argv", ["jokepy", "-n", "100"]):
            error_output = io.StringIO()
            with redirect_stderr(error_output):
                with pytest.raises(SystemExit) as exc_info:
                    main()
                assert exc_info.value.code == 1
            error_result = error_output.getvalue()
            assert "Le nombre maximum de blagues est 50" in error_result
