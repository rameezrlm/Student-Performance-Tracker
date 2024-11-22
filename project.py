class Student:
    def init(self, name, scores):
        self.name = name
        self.scores = scores
    
    def calculate_average(self):
        return sum(self.scores) / len(self.scores)
    
    def is_passing(self):
        return all(score >= 40 for score in self.scores)

class PerformanceTracker:
    def init(self):
        self.students = {}
    
    def add_student(self, name, scores):
        self.students[name] = Student(name, scores)
    
    def calculate_class_average(self):
        total_score = sum(student.calculate_average() for student in self.students.values())
        return total_score / len(self.students)
    
    def display_student_performance(self):
        for student in self.students.values():
            avg = student.calculate_average()
            status = "Passing" if student.is_passing() else "Failing"
            print(f"Student: {student.name}, Average Score: {avg:.2f}, Status: {status}")

# Main program to handle input
def main():
    tracker = PerformanceTracker()
    
    while True:
        try:
            name = input("Enter student's name: ")
            scores = []
            for subject in ['Math', 'Science', 'English']:
                score = int(input(f"Enter score for {subject}: "))
                scores.append(score)
            
            tracker.add_student(name, scores)
            
            continue_input = input("Do you want to add another student? (yes/no): ").lower()
            if continue_input != 'yes':
                break
        except ValueError:
            print("Invalid input! Please enter numeric values for the scores.")
    
    # Display results
    tracker.display_student_performance()
    class_avg = tracker.calculate_class_average()
    print(f"Class Average: {class_avg:.2f}")

# Run the program
if name == "main":
    main()