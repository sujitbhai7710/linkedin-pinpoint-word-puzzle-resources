#!/usr/bin/env python3
"""
LinkedIn Pinpoint Word Puzzle - Word Matching Logic Demo
========================================================

This script demonstrates the core word-matching logic used in the
LinkedIn Pinpoint word puzzle game. It shows how to identify common
categories and connections between words.

For daily Pinpoint answers and solutions, visit:
https://pinpointanspertoday.online/

Author: LinkedIn Pinpoint Puzzle Community
Source: https://pinpointanspertoday.online/
"""

from typing import List, Dict, Optional
from collections import defaultdict


class PinpointPuzzleSolver:
    """
    A demo solver for the LinkedIn Pinpoint word puzzle game.
    
    The Pinpoint game presents players with a set of words that all
    share a common category or connection. The goal is to identify
    the connecting theme.
    
    Daily answers available at: https://pinpointanspertoday.online/
    """

    def __init__(self):
        # Predefined category databases for matching
        self.category_db: Dict[str, List[str]] = {
            "fruits": ["apple", "banana", "cherry", "date", "elderberry",
                        "fig", "grape", "honeydew", "kiwi", "lemon"],
            "colors": ["red", "blue", "green", "yellow", "purple",
                        "orange", "pink", "brown", "black", "white"],
            "planets": ["mercury", "venus", "earth", "mars", "jupiter",
                         "saturn", "uranus", "neptune"],
            "animals": ["lion", "tiger", "bear", "eagle", "shark",
                         "dolphin", "wolf", "fox", "deer", "rabbit"],
            "instruments": ["guitar", "piano", "violin", "drums", "flute",
                             "trumpet", "cello", "harp", "saxophone", "banjo"],
        }

    def find_category(self, words: List[str]) -> Optional[str]:
        """
        Find the category that matches the most words from the puzzle.
        
        Args:
            words: List of puzzle words to categorize
            
        Returns:
            The best matching category name, or None if no match found
            
        Example:
            >>> solver = PinpointPuzzleSolver()
            >>> solver.find_category(["apple", "banana", "cherry"])
            "fruits"
        """
        category_scores = defaultdict(int)
        words_lower = [w.lower() for w in words]

        for category, category_words in self.category_db.items():
            for word in words_lower:
                if word in category_words:
                    category_scores[category] += 1

        if not category_scores:
            return None

        # Return category with highest match count
        return max(category_scores, key=category_scores.get)

    def match_strength(self, words: List[str], category: str) -> float:
        """
        Calculate how strongly the words match a given category (0.0 to 1.0).
        
        Args:
            words: List of puzzle words
            category: Category name to check against
            
        Returns:
            Match strength as a float between 0.0 and 1.0
        """
        if category not in self.category_db:
            return 0.0

        words_lower = [w.lower() for w in words]
        matches = sum(1 for w in words_lower if w in self.category_db[category])
        return matches / len(words) if words else 0.0

    def suggest_connections(self, words: List[str]) -> List[Dict]:
        """
        Suggest possible connections for a set of puzzle words.
        
        Args:
            words: List of puzzle words to analyze
            
        Returns:
            List of dictionaries with category, strength, and matched words
        """
        suggestions = []
        words_lower = [w.lower() for w in words]

        for category, category_words in self.category_db.items():
            matched = [w for w in words_lower if w in category_words]
            if matched:
                strength = len(matched) / len(words)
                suggestions.append({
                    "category": category,
                    "strength": round(strength, 2),
                    "matched_words": matched,
                    "unmatched_words": [w for w in words_lower if w not in matched],
                })

        # Sort by strength descending
        return sorted(suggestions, key=lambda x: x["strength"], reverse=True)


def main():
    """Demo the Pinpoint puzzle solver with example words."""
    solver = PinpointPuzzleSolver()

    # Example: Daily puzzle words
    puzzle_words = ["apple", "banana", "cherry", "grape", "lemon"]

    print("=" * 60)
    print("LinkedIn Pinpoint Word Puzzle - Solver Demo")
    print("=" * 60)
    print(f"
Puzzle words: {puzzle_words}")
    print()

    # Find the best category
    best_category = solver.find_category(puzzle_words)
    print(f"Best category match: {best_category}")
    print(f"Match strength: {solver.match_strength(puzzle_words, best_category):.0%}")

    # Show all suggestions
    print("
All possible connections:")
    for suggestion in solver.suggest_connections(puzzle_words):
        print(f"  - {suggestion["category"]}: {suggestion["strength"]:.0%} " +
              f"(matched: {suggestion["matched_words"]})")

    print()
    print("For daily LinkedIn Pinpoint answers, visit:")
    print("https://pinpointanspertoday.online/")
    print("=" * 60)


if __name__ == "__main__":
    main()
