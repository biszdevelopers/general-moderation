"""Word list loader for the sensitive-stop-words submodule.

The submodule stores one file per category with two supported delimiters:
comma-separated (political, porn) and newline-separated (gun, ad, url,
stopwords). Files are loaded lazily and cached; a missing submodule or a
missing file degrades to an empty list so the service stays operational.
"""

from __future__ import annotations

from pathlib import Path

# Category name -> (file name, delimiter). Delimiter "\n" means one term
# per line; anything else splits the whole file on that character.
_CATEGORY_FILES: dict[str, tuple[str, str]] = {
    "political": ("政治类.txt", ","),
    "porn": ("色情类.txt", ","),
    "gun": ("涉枪涉爆违法信息关键词.txt", "\n"),
    "ad": ("广告.txt", "\n"),
    "url": ("网址.txt", "\n"),
    "stopwords": ("stopword.dic", "\n"),
}

# Categories whose terms are decisive block triggers. ``stopwords`` is a
# preprocessing list of common characters/punctuation and would flag nearly
# every sentence, so it is excluded from blocking.
_BLOCKING_CATEGORIES: tuple[str, ...] = ("political", "porn", "gun", "ad", "url")


class SensitiveWordLoader:
    """Load and cache the external sensitive-word lists.

    :param base_dir: directory containing the submodule files
    """

    def __init__(self, base_dir: str | Path) -> None:
        self._base_dir: Path = Path(base_dir)
        self._cache: dict[str, tuple[str, ...]] = {}

    @property
    def base_dir(self) -> Path:
        """Return the submodule directory."""
        return self._base_dir

    def available(self) -> bool:
        """Whether the submodule directory exists."""
        return self._base_dir.is_dir()

    def load_category(self, category: str) -> tuple[str, ...]:
        """Return the deduplicated words for one category.

        :param category: key into :data:`_CATEGORY_FILES`
        :return: the sorted, stripped words, or an empty tuple
        """
        spec: tuple[str, str] | None = _CATEGORY_FILES.get(category)
        if spec is None:
            return ()
        if category in self._cache:
            return self._cache[category]
        words: tuple[str, ...] = self._parse(self._base_dir / spec[0], spec[1])
        self._cache[category] = words
        return words

    def loaded_categories(self) -> list[str]:
        """List the categories that produced at least one word.

        :return: category names with non-empty files
        """
        return [category for category in _CATEGORY_FILES if self.load_category(category)]

    def all_words(self) -> tuple[str, ...]:
        """Merge every blocking category into one sorted tuple.

        :return: the union of the blocking category words
        """
        combined: set[str] = set()
        for category in _BLOCKING_CATEGORIES:
            combined.update(self.load_category(category))
        return tuple(sorted(combined))

    def reload(self) -> None:
        """Drop the cached words so the next load re-reads the files."""
        self._cache.clear()

    def _parse(self, path: Path, delimiter: str) -> tuple[str, ...]:
        """Read a file and split it on the category delimiter.

        :param path: the list file
        :param delimiter: the separator between terms
        :return: the sorted, stripped, deduplicated words
        """
        if not path.is_file():
            return ()
        try:
            content: str = path.read_text(encoding="utf-8")
        except OSError:
            return ()
        parts: list[str] = content.splitlines() if delimiter == "\n" else content.split(delimiter)
        return tuple(sorted({part.strip() for part in parts if part.strip()}))
