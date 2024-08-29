import pytest
from code_runner import run_code_in_docker
def get_test_cases(language):
    if language == "Java":
        return [
            
            (
                """
                public class Main {
                    public static void main(String[] args) {
                        int a = 5;
                        int b = 10;
                        System.out.println(a + b);
                    }
                }
                """, "15"  # Variables test
            ),
            (
                """
                public class Main {
                    public static void main(String[] args) {
                        int a = 5;
                        if (a > 3) {
                            System.out.println("Greater");
                        } else {
                            System.out.println("Lesser");
                        }
                    }
                }
                """, "Greater"  # Conditional statement test
            ),
            (
                """
                public class Main {
                    public static void main(String[] args) {
                        for (int i = 0; i < 5; i++) {
                            System.out.println(i);
                        }
                    }
                }
                """,
                "0\n1\n2\n3\n4"  # Loop test
            ),
        ]
    elif language == "C":
        return [
            (
                """
                #include <stdio.h>
                int main() {
                    int a = 5;
                    int b = 10;
                    printf("%d\\n", a + b);
                    return 0;
                }
                """, "15\n"  # Variables test
            ),
            (
                """
                #include <stdio.h>
                int main() {
                    int a = 5;
                    if (a > 3) {
                        printf("Greater\\n");
                    } else {
                        printf("Lesser\\n");
                    }
                    return 0;
                }
                """, "Greater\n"  # Conditional statement test
            ),
            (
                """
                #include <stdio.h>
                int main() {
                    for (int i = 0; i < 5; i++) {
                        printf("%d\\n", i);
                    }
                    return 0;
                }
                """, "0\n1\n2\n3\n4\n"  # Loop test
            ),
        ]

