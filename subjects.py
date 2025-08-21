import random
import math
import numpy as np
from typing import Dict, List, Tuple, Any

class SubjectManager:
    """Manages subject-specific content and functionality"""
    
    def __init__(self):
        self.subjects_data = self._initialize_subjects_data()
    
    def _initialize_subjects_data(self) -> Dict[str, Any]:
        """Initialize comprehensive subject data"""
        return {
            "Mathematics": {
                "concepts": [
                    "algebra", "geometry", "calculus", "trigonometry", "statistics",
                    "probability", "linear algebra", "differential equations", "number theory"
                ],
                "random_problems": {
                    "Beginner": [
                        "Solve for x: 2x + 5 = 15",
                        "Find the area of a circle with radius 3",
                        "What is 15% of 80?",
                        "Solve: 3x - 7 = 14",
                        "Calculate: (4 + 6) × 2"
                    ],
                    "Intermediate": [
                        "Solve the quadratic equation: x² - 5x + 6 = 0",
                        "Find the derivative of f(x) = 3x² + 2x - 1",
                        "Calculate the volume of a sphere with radius 4",
                        "Solve the system: 2x + y = 7, x - y = 2",
                        "Find sin(60°) without a calculator"
                    ],
                    "Advanced": [
                        "Prove that the derivative of sin(x) is cos(x)",
                        "Find the limit: lim(x→0) (sin(x)/x)",
                        "Solve the differential equation: dy/dx = 2xy",
                        "Calculate the eigenvalues of the matrix [[2,1],[1,2]]",
                        "Prove the fundamental theorem of calculus"
                    ]
                },
                "formulas": {
                    "Basic": {
                        "Area of rectangle": "A = length × width",
                        "Area of circle": "A = πr²",
                        "Pythagorean theorem": "a² + b² = c²",
                        "Quadratic formula": "x = (-b ± √(b²-4ac)) / 2a"
                    },
                    "Advanced": {
                        "Derivative power rule": "d/dx(xⁿ) = nx^(n-1)",
                        "Integration by parts": "∫udv = uv - ∫vdu",
                        "Chain rule": "d/dx[f(g(x))] = f'(g(x))·g'(x)",
                        "Fundamental theorem of calculus": "∫[a,b]f'(x)dx = f(b) - f(a)"
                    }
                }
            },
            "Physics": {
                "concepts": [
                    "mechanics", "thermodynamics", "electromagnetism", "optics", "quantum physics",
                    "relativity", "waves", "atomic physics", "nuclear physics"
                ],
                "random_problems": {
                    "Beginner": [
                        "A car travels 60 km in 2 hours. What is its average speed?",
                        "Calculate the weight of a 5 kg object on Earth (g = 9.8 m/s²)",
                        "How much work is done lifting a 10 N object 2 meters high?",
                        "What is the kinetic energy of a 2 kg ball moving at 5 m/s?",
                        "A force of 20 N acts on a 4 kg mass. What is the acceleration?"
                    ],
                    "Intermediate": [
                        "A projectile is launched at 30° with initial velocity 20 m/s. Find its range.",
                        "Calculate the period of a pendulum with length 1 meter",
                        "Find the electric field at distance r from a point charge q",
                        "What is the frequency of light with wavelength 500 nm?",
                        "Calculate the power dissipated in a 10Ω resistor with 2A current"
                    ],
                    "Advanced": [
                        "Derive the wave equation from Maxwell's equations",
                        "Calculate the binding energy of a hydrogen atom",
                        "Find the Schwarzschild radius of a black hole with mass M",
                        "Solve Schrödinger's equation for a particle in a box",
                        "Calculate the relativistic momentum of a particle at 0.8c"
                    ]
                },
                "formulas": {
                    "Mechanics": {
                        "Newton's second law": "F = ma",
                        "Kinematic equation": "v² = u² + 2as",
                        "Kinetic energy": "KE = ½mv²",
                        "Potential energy": "PE = mgh"
                    },
                    "Electromagnetism": {
                        "Coulomb's law": "F = kq₁q₂/r²",
                        "Ohm's law": "V = IR",
                        "Power": "P = VI = I²R = V²/R",
                        "Magnetic force": "F = qvBsinθ"
                    }
                }
            },
            "Chemistry": {
                "concepts": [
                    "atomic structure", "chemical bonding", "stoichiometry", "thermochemistry",
                    "kinetics", "equilibrium", "acids and bases", "electrochemistry", "organic chemistry"
                ],
                "random_problems": {
                    "Beginner": [
                        "Balance the equation: H₂ + O₂ → H₂O",
                        "How many protons does carbon have?",
                        "What is the molar mass of water (H₂O)?",
                        "Calculate moles in 44g of CO₂",
                        "What type of bond forms between Na and Cl?"
                    ],
                    "Intermediate": [
                        "Calculate the pH of a 0.01 M HCl solution",
                        "How many grams of NaCl are needed to make 500 mL of 0.2 M solution?",
                        "Balance and complete: C₄H₁₀ + O₂ → CO₂ + H₂O",
                        "Calculate the equilibrium constant for A + B ⇌ C + D",
                        "Determine the oxidation state of sulfur in H₂SO₄"
                    ],
                    "Advanced": [
                        "Calculate the enthalpy change for a reaction using bond energies",
                        "Determine the rate law for a complex reaction mechanism",
                        "Calculate the cell potential for a galvanic cell",
                        "Predict the products of an SN2 reaction",
                        "Calculate the pH of a buffer solution"
                    ]
                },
                "formulas": {
                    "Basic": {
                        "Ideal gas law": "PV = nRT",
                        "Molarity": "M = moles/liters",
                        "pH": "pH = -log[H⁺]",
                        "Density": "ρ = m/V"
                    },
                    "Advanced": {
                        "Arrhenius equation": "k = Ae^(-Ea/RT)",
                        "Nernst equation": "E = E° - (RT/nF)lnQ",
                        "Henderson-Hasselbalch": "pH = pKa + log([A⁻]/[HA])",
                        "Gibbs free energy": "ΔG = ΔH - TΔS"
                    }
                }
            },
            "Biology": {
                "concepts": [
                    "cell biology", "genetics", "evolution", "ecology", "physiology",
                    "molecular biology", "biochemistry", "anatomy", "microbiology"
                ],
                "random_problems": {
                    "Beginner": [
                        "What are the main differences between plant and animal cells?",
                        "Explain the process of photosynthesis in simple terms",
                        "What is DNA and where is it found?",
                        "Name the levels of biological organization",
                        "What is the function of mitochondria?"
                    ],
                    "Intermediate": [
                        "Explain how genetic traits are passed from parents to offspring",
                        "Describe the process of cellular respiration",
                        "What is natural selection and how does it work?",
                        "Explain the difference between mitosis and meiosis",
                        "How do enzymes work as biological catalysts?"
                    ],
                    "Advanced": [
                        "Explain the molecular mechanism of DNA replication",
                        "Describe the process of protein synthesis from gene to protein",
                        "How do mutations contribute to genetic diversity and disease?",
                        "Explain the regulation of gene expression in eukaryotes",
                        "Describe the molecular basis of evolution at the genetic level"
                    ]
                }
            },
            "Computer Science": {
                "concepts": [
                    "programming", "algorithms", "data structures", "databases", "networks",
                    "software engineering", "artificial intelligence", "cybersecurity", "machine learning"
                ],
                "random_problems": {
                    "Beginner": [
                        "What is a variable in programming?",
                        "Explain the difference between a list and a dictionary",
                        "What is a loop and when would you use one?",
                        "What is the difference between == and = in programming?",
                        "Explain what a function is and why it's useful"
                    ],
                    "Intermediate": [
                        "Implement a binary search algorithm",
                        "Explain the time complexity of bubble sort",
                        "What is recursion and when should you use it?",
                        "Design a simple database schema for a library system",
                        "Explain the difference between stack and queue data structures"
                    ],
                    "Advanced": [
                        "Implement a balanced binary search tree",
                        "Explain the principles of dynamic programming",
                        "Design a distributed system architecture",
                        "Implement a neural network from scratch",
                        "Explain different sorting algorithms and their trade-offs"
                    ]
                }
            }
        }
    
    def get_random_concept(self, subject: str) -> str:
        """Get a random concept from the specified subject"""
        if subject in self.subjects_data:
            concepts = self.subjects_data[subject]["concepts"]
            return random.choice(concepts)
        return "general learning"
    
    def get_random_problem(self, subject: str, level: str) -> str:
        """Get a random practice problem for the subject and level"""
        if subject in self.subjects_data and "random_problems" in self.subjects_data[subject]:
            problems = self.subjects_data[subject]["random_problems"].get(level, [])
            if problems:
                return random.choice(problems)
        return f"Practice problem for {subject} at {level} level"
    
    def get_formulas(self, subject: str, complexity: str = "Basic") -> Dict[str, str]:
        """Get relevant formulas for a subject"""
        if subject in self.subjects_data and "formulas" in self.subjects_data[subject]:
            return self.subjects_data[subject]["formulas"].get(complexity, {})
        return {}
    
    def get_subject_overview(self, subject: str) -> str:
        """Get an overview of the subject"""
        overviews = {
            "Mathematics": "Mathematics is the language of science and engineering. It provides tools for understanding patterns, solving problems, and modeling real-world phenomena. From basic arithmetic to advanced calculus, math builds logical thinking skills.",
            
            "Physics": "Physics seeks to understand how the universe works, from the smallest particles to the largest galaxies. It explains the fundamental forces and laws that govern matter and energy, providing the foundation for all other sciences.",
            
            "Chemistry": "Chemistry is the study of matter and the changes it undergoes. It bridges physics and biology, explaining how atoms and molecules interact to form the complex substances that make up our world.",
            
            "Biology": "Biology is the study of life in all its forms. From microscopic bacteria to complex ecosystems, biology explores how living organisms function, evolve, and interact with their environment.",
            
            "Computer Science": "Computer Science combines mathematical rigor with engineering innovation. It encompasses programming, algorithms, system design, and the theoretical foundations of computation and information processing."
        }
        
        return overviews.get(subject, f"{subject} is a fascinating field of study with many practical applications.")
    
    def get_career_connections(self, subject: str) -> List[str]:
        """Get career paths related to the subject"""
        careers = {
            "Mathematics": [
                "Data Scientist", "Actuary", "Mathematician", "Statistician", "Financial Analyst",
                "Software Engineer", "Research Scientist", "Teacher/Professor", "Engineer"
            ],
            "Physics": [
                "Physicist", "Engineer", "Astronomer", "Medical Physicist", "Research Scientist",
                "Data Scientist", "Software Developer", "Teacher/Professor", "Consultant"
            ],
            "Chemistry": [
                "Chemist", "Chemical Engineer", "Pharmacist", "Materials Scientist", "Forensic Scientist",
                "Environmental Scientist", "Research Scientist", "Quality Control Analyst", "Teacher"
            ],
            "Biology": [
                "Biologist", "Doctor", "Veterinarian", "Pharmacist", "Geneticist", "Ecologist",
                "Biotechnologist", "Research Scientist", "Teacher", "Environmental Consultant"
            ],
            "Computer Science": [
                "Software Engineer", "Data Scientist", "Cybersecurity Specialist", "AI/ML Engineer",
                "Web Developer", "Game Developer", "System Administrator", "Product Manager", "Researcher"
            ]
        }
        
        return careers.get(subject, ["Various career opportunities available"])
    
    def get_real_world_applications(self, subject: str) -> List[str]:
        """Get real-world applications of the subject"""
        applications = {
            "Mathematics": [
                "GPS navigation systems", "Computer graphics and animation", "Financial modeling",
                "Medical imaging", "Weather prediction", "Cryptography and security"
            ],
            "Physics": [
                "Smartphone technology", "Medical imaging (X-rays, MRI)", "Solar panels and renewable energy",
                "Laser surgery", "Satellite communications", "Particle accelerators"
            ],
            "Chemistry": [
                "Drug development", "Materials science (plastics, metals)", "Food preservation",
                "Cleaning products", "Batteries and energy storage", "Environmental remediation"
            ],
            "Biology": [
                "Medicine and healthcare", "Agriculture and food production", "Environmental conservation",
                "Biotechnology and genetic engineering", "Forensic science", "Biofuels"
            ],
            "Computer Science": [
                "Social media platforms", "Search engines", "Online banking", "Video games",
                "Artificial intelligence", "Autonomous vehicles", "E-commerce"
            ]
        }
        
        return applications.get(subject, ["Many practical applications in daily life"])
    
    def get_study_resources(self, subject: str, level: str) -> Dict[str, List[str]]:
        """Get recommended study resources for a subject and level"""
        resources = {
            "Mathematics": {
                "Beginner": [
                    "Khan Academy Math Basics", "PatrickJMT YouTube channel",
                    "Math textbooks with lots of practice problems", "Photomath app for step-by-step solutions"
                ],
                "Intermediate": [
                    "Paul's Online Math Notes", "Khan Academy Advanced Math",
                    "Stewart Calculus textbook", "Wolfram Alpha for verification"
                ],
                "Advanced": [
                    "MIT OpenCourseWare", "Wolfram MathWorld", "Mathematical journals",
                    "Research papers and advanced textbooks"
                ]
            },
            "Physics": {
                "Beginner": [
                    "Khan Academy Physics", "Crash Course Physics", "Conceptual Physics textbook",
                    "Physics simulation apps"
                ],
                "Intermediate": [
                    "Feynman Lectures on Physics", "Physics Classroom website",
                    "University Physics textbooks", "PhET simulations"
                ],
                "Advanced": [
                    "MIT Physics courses", "Physics journals", "Griffiths textbooks",
                    "Research publications"
                ]
            }
        }
        
        return resources.get(subject, {}).get(level, ["General study materials and online resources"])
    
    def get_prerequisite_knowledge(self, subject: str, level: str) -> List[str]:
        """Get prerequisite knowledge for studying a subject at a given level"""
        prerequisites = {
            "Mathematics": {
                "Beginner": ["Basic arithmetic", "Understanding of numbers"],
                "Intermediate": ["Algebra", "Basic geometry", "Trigonometry"],
                "Advanced": ["Calculus", "Linear algebra", "Differential equations"]
            },
            "Physics": {
                "Beginner": ["Basic math", "Scientific notation"],
                "Intermediate": ["Algebra", "Trigonometry", "Basic calculus"],
                "Advanced": ["Multivariable calculus", "Differential equations", "Linear algebra"]
            },
            "Chemistry": {
                "Beginner": ["Basic math", "Scientific notation"],
                "Intermediate": ["Algebra", "Basic physics concepts"],
                "Advanced": ["Calculus", "Physical chemistry", "Quantum mechanics basics"]
            }
        }
        
        return prerequisites.get(subject, {}).get(level, ["Basic foundation in the subject area"])

class MathSolver:
    """Specialized math problem solver"""
    
    @staticmethod
    def solve_linear_equation(equation: str) -> str:
        """Solve simple linear equations"""
        # This is a simplified solver for educational purposes
        try:
            # Remove spaces and split by =
            equation = equation.replace(" ", "")
            left, right = equation.split("=")
            
            # For very simple cases like "2x+3=7"
            if "x" in left and "x" not in right:
                # Basic pattern matching for simple linear equations
                return f"To solve {equation}:\n1. Isolate the x term\n2. Perform inverse operations\n3. Simplify\n\nThis would involve moving constants and solving for x."
            
        except:
            pass
        
        return f"To solve the equation '{equation}', I recommend these steps:\n1. Identify the variable\n2. Move all terms with the variable to one side\n3. Move all constants to the other side\n4. Simplify both sides\n5. Solve for the variable"
    
    @staticmethod
    def calculate_area(shape: str, **kwargs) -> str:
        """Calculate area of different shapes"""
        if shape.lower() == "circle":
            radius = kwargs.get("radius", 1)
            area = math.pi * radius ** 2
            return f"Area of circle with radius {radius}: {area:.2f} square units"
        
        elif shape.lower() == "rectangle":
            length = kwargs.get("length", 1)
            width = kwargs.get("width", 1)
            area = length * width
            return f"Area of rectangle ({length} × {width}): {area} square units"
        
        elif shape.lower() == "triangle":
            base = kwargs.get("base", 1)
            height = kwargs.get("height", 1)
            area = 0.5 * base * height
            return f"Area of triangle (base: {base}, height: {height}): {area} square units"
        
        return f"I can calculate area for circles, rectangles, and triangles. Please specify the shape and dimensions."

class PhysicsSimulator:
    """Physics problem simulator and solver"""
    
    @staticmethod
    def projectile_motion(velocity: float, angle: float) -> Dict[str, float]:
        """Calculate projectile motion parameters"""
        g = 9.81  # gravity
        angle_rad = math.radians(angle)
        
        # Calculate key parameters
        time_flight = 2 * velocity * math.sin(angle_rad) / g
        max_height = (velocity * math.sin(angle_rad)) ** 2 / (2 * g)
        range_distance = velocity ** 2 * math.sin(2 * angle_rad) / g
        
        return {
            "time_of_flight": round(time_flight, 2),
            "maximum_height": round(max_height, 2),
            "range": round(range_distance, 2)
        }
    
    @staticmethod
    def kinetic_energy(mass: float, velocity: float) -> float:
        """Calculate kinetic energy"""
        return 0.5 * mass * velocity ** 2
    
    @staticmethod
    def potential_energy(mass: float, height: float, g: float = 9.81) -> float:
        """Calculate gravitational potential energy"""
        return mass * g * height

class ChemicalEquationBalancer:
    """Chemical equation balancer and chemistry helper"""
    
    @staticmethod
    def balance_simple_equation(equation: str) -> str:
        """Provide guidance for balancing chemical equations"""
        return f"To balance the equation '{equation}':\n\n1. Count atoms of each element on both sides\n2. Add coefficients to balance each element\n3. Start with the most complex molecule\n4. Balance metals first, then non-metals\n5. Balance oxygen and hydrogen last\n6. Check that all atoms are balanced\n\nWould you like me to walk through a specific example?"
    
    @staticmethod
    def calculate_molar_mass(formula: str) -> str:
        """Calculate molar mass guidance"""
        return f"To calculate the molar mass of {formula}:\n\n1. Identify each element in the formula\n2. Count how many atoms of each element\n3. Look up atomic masses from periodic table\n4. Multiply atomic mass by number of atoms\n5. Add up all the masses\n\nExample: For H₂O = (2×1.008) + (1×15.999) = 18.015 g/mol"
