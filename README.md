# RecruitmentProcess

Przygotowałem 2 testy
Pierwszy dodaje nowego użytkownika z poziomu już zalogowanego użytkownika
Drugi sprawdza czy wysyłane jest link ze zmianą hasła

Testy możemy odpalić na 2 sposoby:

Python TestRunner.py
lub

Python Test_AddNewUser.py
Python Test_ResetPassword.py

Z obu plików usunąłem hasło do swojego konta.
Aby puścić test należy wpisać własny adres i hasło
 (UWAGA ResetPassword kasuje wszystkie emaile na danym koncie email)

W pliku EnvironmentSetUp.py należy podać ścieżkę do Chromedrivera, który też należy
dodać do projektu.
