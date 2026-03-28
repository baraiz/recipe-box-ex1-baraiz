from __future__ import annotations

from typing import Dict

from .models import Recipe, RecipeCreate


class RecipeRepository:
    """In-memory storage for recipes."""

    def __init__(self) -> None:
        self._items: Dict[int, Recipe] = {}
        self._next_id = 1

    def list(self) -> list[Recipe]:
        """Get all recipes."""
        return list(self._items.values())

    def create(self, payload: RecipeCreate) -> Recipe:
        """Add a new recipe and return it with assigned ID."""
        recipe = Recipe(id=self._next_id, **payload.model_dump())
        self._items[recipe.id] = recipe
        self._next_id += 1
        return recipe

    def get(self, recipe_id: int) -> Recipe | None:
        """Get a recipe by ID, or None if not found."""
        return self._items.get(recipe_id)

    def delete(self, recipe_id: int) -> None:
        """Remove a recipe by ID."""
        self._items.pop(recipe_id, None)

    def clear(self) -> None:
        """Remove all recipes (useful for tests)."""
        self._items.clear()
        self._next_id = 1