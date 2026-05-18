"""Shared data models for the humanoid robot learning paper pipeline."""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Paper(BaseModel):
    arxiv_id: str
    title: str
    paper_url: str
    project_url: Optional[str] = None
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
