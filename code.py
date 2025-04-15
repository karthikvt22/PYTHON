# Terraform Course Tracker 🛠️
# Author: Karthik V T
# Description: Python project to track progress of Terraform one-shot video course.

import json
from datetime import datetime
import os

class TerraformCourseTracker:
    def __init__(self, filename="terraform_tracker.json"):
        self.filename = filename
        self.sections = []
        if os.path.exists(filename):
            self.load_from_file()
        else:
            self.initialize_sections()

    def initialize_sections(self):
        timestamps = [
            ("00:00", "Introduction"),
            ("00:56", "What is Terraform?"),
            ("01:26", "Course Overview"),
            ("02:47", "Reference Architecture"),
            ("04:11", "Part 1: Evolution of Cloud + Infrastructure as Code"),
            ("14:36", "Part 2: Terraform Overview + Setup"),
            ("20:13", "Part 2 Demo"),
            ("28:32", "Part 3: Basic Terraform Usage"),
            ("45:11", "Part 3 Demo"),
            ("58:23", "Part 4: Variables and Outputs"),
            ("1:05:14", "Part 4 Demo"),
            ("1:11:20", "Part 5: Additional Language Features"),
            ("1:20:02", "Part 6: Project Organization + Modules"),
            ("1:29:00", "Part 6 Demo"),
            ("1:36:06", "Part 7: Managing Multiple Environments"),
            ("1:44:29", "Part 7 Demo"),
            ("1:56:05", "Part 8: Testing Terraform Code"),
            ("2:03:32", "Part 8 Demo"),
            ("2:13:04", "Part 9: Developer Workflows and Automation"),
            ("2:25:09", "Part 9 Demo"),
            ("2:36:24", "Wrap up!")
        ]
        for timestamp, title in timestamps:
            self.sections.append({
                "timestamp": timestamp,
                "title": title,
                "completed": False,
                "notes": ""
            })
        self.save_to_file()

    def mark_completed(self, title):
        for section in self.sections:
            if section["title"].lower() == title.lower():
                section["completed"] = True
                section["completed_at"] = datetime.now().isoformat()
                self.save_to_file()
                return f" Marked '{title}' as completed."
        return f" Section '{title}' not found."

    def add_notes(self, title, notes):
        for section in self.sections:
            if section["title"].lower() == title.lower():
                section["notes"] = notes
                self.save_to_file()
                return f"Notes added to '{title}'."
        return f" Section '{title}' not found."

    def save_to_file(self):
        with open(self.filename, "w") as f:
            json.dump(self.sections, f, indent=4)

    def load_from_file(self):
        with open(self.filename, "r") as f:
            self.sections = json.load(f)

    def show_progress(self):
        print("\n Terraform Course Progress:")
        for section in self.sections:
            status = "YES" if section["completed"] else "NO"
            print(f"{status} {section['timestamp']} - {section['title']}")

    def run_menu(self):
        while True:
            print("\n--- Terraform Course Tracker Menu ---")
            print("1. Show Progress")
            print("2. Mark Section as Completed")
            print("3. Add Notes to Section")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_progress()
            elif choice == "2":
                title = input("Enter section title to mark completed: ")
                print(self.mark_completed(title))
            elif choice == "3":
                title = input("Enter section title to add notes: ")
                notes = input("Enter your notes: ")
                print(self.add_notes(title, notes))
            elif choice == "4":
                print(" Exiting. Happy learning!")
                break
            else:
                print(" Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = TerraformCourseTracker()
    tracker.run_menu()
