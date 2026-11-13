"""Shared data models for the humanoid robot learning paper pipeline."""

from pydantic import BaseModel, Field, model_validator
from typing import Optional, Literal
from datetime import date


class Paper(BaseModel):
    arxiv_id: str
    title: str
    paper_url: str
    project_url: Optional[str] = None
    repository_url: Optional[str] = None
    comments: str = ""
    code_status: Literal["unverified", "not_found", "no_repository", "coming_soon", "empty", "partial", "available", "unknown"] = "unverified"
    code_evidence: list[str] = Field(default_factory=list)
    code_checked_at: Optional[str] = None
    authors: list[str] = []
    published: str = ""  # "2026-04"
    published_date: Optional[date] = None
    abstract: str = ""
    categories: list[str] = []
    tags: list[str] = []
    real_robot: bool = False
    open_source: bool = False
    platform: Optional[str] = None
    summary: str = ""
    primary_category: str = ""

    @model_validator(mode="after")
    def normalize_code_flag(self):
        # Legacy URL-only flags must not be presented as verified code releases.
        self.open_source = self.code_status == "available"
        return self
