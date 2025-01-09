*You should take the approach that you're wrong. Your goal is to be less wrong.* — ***Elon Musk***

---

# Webservices
This project is for personal practice. I will have an entry test for a job application in a week. All I know is that I will need to implement a webservice within a specified time interval. I can pick the technology for the task freely.
## Stack
Given that the position is a backend one with keywords like `Python`, `Relational Databases`, `REST`, `NoSQL`, `Microservices` and so on, I chose to study **[FastAPI](https://fastapi.tiangolo.com/)** - and for an extra challenge **[MongoDB](https://www.mongodb.com/)**.
## TODOs
The plan is that during the learning process I will be able to abstract away elements so that in the end I will have a small but general enough codebase to use it for copy-pasting.

### Subprojects
- [x] fastapi-crud
- [x] fastapi-postgres-crud (due to lack of time automatic tests and HATEOAS are not implemented)
- [x] fastapi-mongodb-crud (due to lack of time 'checks/{id}/procedures' GET is not implemented)
- [ ] fastapi-mongodb-auth
- [ ] fastapi-files
- [ ] fastapi-bgtasks
- [ ] fastapi-something

## Subproject workflow - at the moment
1. `mkdir` and `cd` to subproject folder
2. `git checkout -b subproject-branch`
3. create project structure
4. `venv`, activate, install requirements
5. create `main.py`, `config.py`, `session.py`, `api.py` files (+ `.env`)
6. code db models
7. code schemas
8. code routes
9. megre branch mack to `master` then delete
10. GOTO 1

## Conclusion

### **At the starting line**
First day of studying was on 19 Aug. 2022 - 9 days ago. At the beginning I did not exactly know what `REST` and `NoSQL` were. **[FastAPI](https://fastapi.tiangolo.com/)**, **[pydantic](https://pydantic-docs.helpmanual.io/)**, **[MongoDB](https://www.mongodb.com/)** and **[Beanie](https://roman-right.github.io/beanie/)** were completely new. I have never used **[SQLAlchemy](https://www.sqlalchemy.org/)** code-first. Also I did not use **[venv](https://docs.python.org/3/library/venv.html)** and **[git](https://git-scm.com/)** properly.

### **Close to the finish line**
`NoSQL` is still a blurry concept - although I have some idea what a document-oriented database is. I only scratched the surface but thinking in `REST` style seems a fairly simple and attractive path to me.

**venv** and **git** are nothing special, but useful tools.

**SQLAclhemy** is just a must - if it is relational I would rather write **SQL** code.

**MongoDB** with the **FastAPI**-**Pydantic**-**Beanie** triad are truly amazing! These are such technologies I definitely want to dive deeper into later. The smartness of these tools what makes me interested. Reading the documentations was kind of a similar experience to learning math - I enjoyed seeing more clearly than before.

## Self-reflecion before test

I tought for learning the basics through the set subproject goals, a week and a half would be enough - turns out it is rather a 4-6 week long process. Coding time was underestimated and in addition I did not calculate with technical issues. 

When I learn I do not memorize but understand, thus if there will be any type of task which I did not implement at least once, I am completely dead. Relying on Google and documentation seems too slow to me for the given time interval...

## Self-reflection after test

Well... I should have done some experiment with deploying at least once. There was a lack of understanding about how [PyInstaller](https://pyinstaller.org/en/stable/) and [Docker](https://www.docker.com/) works. Otherwise the test was so much easier than I expected. Besides deploying, the only thing bugging me is the missing information about input types in the specification...

## Future of the project

This week was an intensive one but all in all I liked the pace and the struggle of the journey. As I said I will have more fun with these technologies. But for now, first I need some sleep, second I need to complete a test, third I need to fix my PC, then I have to get back to my clojure side-project because my backlog just grows. Then maybe a week after next week.

;)

**_29 Aug 2022_**