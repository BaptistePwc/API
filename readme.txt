Vous voici sur une API permettant de generer des questions.
Retrouvez ci-dessous des exemples d'appel à l'api à l'aide de la methode curl à effectuer depuis votre terminal.

### Vérifier que l'API est fonctionnelle
shell
curl http://localhost:8000/
>>{"message":"Bienvenue sur votre API de question"}

### Créer une question
shell
curl -X POST -H "Content-Type: application/json" -u admin:4dm1N -d '{"question":"Quelle est la capitale de la France?", "subject":"Géographie", "correct":"Paris", "use":"QCM", "responseA":"Paris", "responseB":"Londres", "responseC":"Berlin"}' http://localhost:8000/questions
>>{"message":"Question créée"}


### Obtenir des questions (ex 5 questions de test de validation à propos de l'Automation)
shell
$ curl -u alice:wonderland http://localhost:8000/questions?count=5&use="Test de validation"&subject="Automation"

>>>
 [{"question":"Dans Airflow, le DAG répertorie","subject":"Automation","use":"Test de validation","correct":"D","responseA":"Les tâches à effectuer","responseB":"Les actions à prendre en cas d'échecs","responseC":"L'enchaînement des tâches à effectuer","responseD":"Tous ces points","remark":""},{"question":"DockerHub est","subject":"Docker","use":"Test de positionnement","correct":"C","responseA":"un système qui permet de lancer plusieurs containers d'un coup","responseB":"un système d'orchestration de containers","responseC":"un répertoire d'images Docker","responseD":"","remark":""},{"question":"Classification","subject":"Machine Learning","use":"Total Bootcamp","correct":"B","responseA":"Is used when the target we aim to predict is continuous.","responseB":"Is used when the target we aim to work on is discrete.","responseC":"Is not a method needing artificial intelligence techniques.","responseD":"","remark":""},{"question":"A quoi sert Docker-Compose ?","subject":"Automation","use":"Test de validation","correct":"B","responseA":"A répertorier les images publiques de containers","responseB":"A déployer plusieurs containers en même temps","responseC":"A créer sa propre image Docker","responseD":"Tous ces points","remark":""},{"question":"Are every datasets worth a Data Science project ?","subject":"Data Science","use":"Total Bootcamp","correct":"A","responseA":"No.","responseB":"If it's big enough, yes.","responseC":"Yes.","responseD":"","remark":""}]