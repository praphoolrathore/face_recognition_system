                    CREATE TABLE IF NOT EXISTS {self.subject} (
                            student_id VARCHAR(10) PRIMARY KEY,
                            name VARCHAR(100),
                            roll VARCHAR(20),
                            dep VARCHAR(50),
                            date DATE,
                            time TIME,
                            status VARCHAR(10)
                        )
                    """)