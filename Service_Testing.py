import User, screen_Builder, Screen, analyzer

risk_profiles = ["Risky", "Moderate", "Defensive"]

investing_knowledge = ["low", "medium", "high"]

areas_of_interest = ["Technology", "REITs"]


def build_test_user():

    safe_user = User.User()
    safe_user.setup_profile("Defensive", "low", "REITs")
    risky_user = User.User()
    risky_user.setup_profile("Risky", "medium", "Technology")
    safe_user.generate_screen_url()
    risky_user.generate_screen_url()

    safe_user.run_all_empty_screen()
    safe_user.get_all_screen_results()
    # risky_user.run_all_empty_screen()

    # risky_user.get_all_screen_results()


def build_screen_url():

    # builds a url using Screen_Builder.py and screen_builder
    print("Service_Testing.py build_screen")
    test_screen = screen_Builder.screen_Builder("X", "Y", "Defensive")
    test_screen.build_screen()
    print("Screen")
    print(test_screen.screen_url)

def run_screen():
    test_screen = screen_Builder.screen_Builder("X", "Y", "Defensive")
    test_screen.build_screen()
    analyzer.exeucute_url(test_screen.screen_url)

build_test_user()