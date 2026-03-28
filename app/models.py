from __future__ import annotations

from pydantic import BaseModel, Field, model_validator


class RecipeBase(BaseModel):
    """Shared fields for create/read models."""
    title: str
    prep_time: int = Field(ge=1, le=1440)  # Preparation time in minutes (up to 24 hours)
    category: str


class Recipe(RecipeBase):
    """Response model that includes the server-generated ID."""
    id: int


class RecipeCreate(RecipeBase):
    """Incoming payload with validation + normalization."""

    @model_validator(mode="after")
    def normalize_category(self) -> "RecipeCreate":
        """Title-case the category: 'cakes' → 'Cakes'."""
        self.category = self.category.title()
        return self