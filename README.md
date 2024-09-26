


> ##  [ToDos](https://avonggeorge.github.io/todos/)
> This a web application for 'Task Management'.
The name was derived from the word ''To-Do'' which generally refers to a list of items on a checklist

## TECHNOLOGY
- Python
- Flask
- Jinja
- HTML
- CSS
- JavaScript
- SQLAlchemy

## How the project was inspired
Our lives everyday is filled with a lot of activities that needs to be carried out especially for student like us learning Full-Stack Software Engineering. We often have too much to juggle with, from studies to practice, projects completion deadlines and other activities including personal stuffs. We have used some task management app that helped us archive some of our goals. So we thought why don't we design a task manager application tailored for students like us and in extension a wider user community. That was when we came up with the idea of a task manager application, and called it "Todos".
## Architecture
**![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUeIIxgB2HlsyabKm-n20dafJyvjjYe7Z-UpUm0bW01gDkF4YzIvPOejJsK03kB4D2a6W_aqRZYkY7k4RJKpXU1nC70sYz5jvATYiuZNC1Q_kNbZ4PsI1IwGtARgAa4_mMn1h4dJp1dIIj_oDBjGztBkabq8s-k=s2048?key=yyyfB7t8_lK0P5d3-FNyAg)**
## APIs and Methods
-   ### API Routes
    

-   **/api/tasks**
    

-   **GET:** Retrieves a list of all tasks for the current user. This endpoint will return task details such as task ID, title, description, due date, and completion status.
    
-   **POST:** Creates a new task for the current user. The request body should include the task title, description, and due date. The server will assign a unique ID and set the initial completion status to false.
    
-   **PUT:** Updates an existing task based on the provided task ID. The request body can include changes to the title, description, due date, or completion status.
    
-   **DELETE:** Deletes a task based on the provided task ID. This operation will permanently remove the task from the database.
    

  

-   **/api/users**
    

-   **GET:** Retrieves the user information based on the session ID. This includes the user's ID, username, and email. It is used to confirm the user's identity and session status.
    
-   **POST:** Creates a new user account. The request body should include the username, email, and password. The server will hash the password before storing it in the database and return a confirmation message upon successful account creation.
    
-   **PUT:** Updates the user's information, such as email or password. The request body should include the updated fields, and the server will ensure that the changes are properly stored.
    
-   **DELETE:** Deletes the user account associated with the session. This will remove the user's data from the database, including all tasks.
-   **/api/login**

-   **POST:** Authenticates the user based on the provided username and password. If successful, this will create a session for the user and return a session token for subsequent requests.

-   **/api/logout**
-   **POST:** Ends the user's session by invalidating the session token. This ensures that the user is logged out securely.

-   **/api/complete_task**
-   **POST:** Marks a specific task as completed based on the provided task ID. The request body should include the task ID, and the server will update the task's completion status to true.

## **Data Model**
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXe3Xov8sI1L6foz2GkAhxORKFJBlDOb-MoAwDzzL-5BmUQvji5JM49DEP6tMviOBe0xQfHlctGZ2V0ocL_IOi0ij2pGNH1bfMjrnpLyDuvM0n17SEOWBMahZo11iuq4pUyEpdsliSGnCgpmmhxNokxQA-Gf?key=4XbUcFGf9gSlmdzegHM0Tg)**
**Entities:**
-   **User**
    

	-   ID (Primary Key)
    
	-   Username
    
	-   Email
    
	-   Password
    

  

-   **Task**
    

	-   ID (Primary Key)
    
	-   Title
    
	-   Description
    
	-   Status (e.g., Pending, In Progress, Completed)
    
	-   Due Date
    
	-   User ID (Foreign Key referencing User)
    

  

-  **Relationships:**
    

	-   A user can have multiple tasks (One-to-Many relationship).

## **User Stories**

  

Below are detailed user stories that will guide the development of the Task Manager MVP:

-   As a user, I want to be able to create new tasks so that I can keep track of my to-do items.
    

	-   Acceptance Criteria: The user can input a task title, description, and due date, and the task will be saved to the database.
    

  

-   As a user, I want to view a list of my tasks so that I can see what I need to do.
    

	-   Acceptance Criteria: The user can see a list of tasks with their current status and due dates.
    

  

-   As a user, I want to update the status of my tasks so that I can track my progress.
    

	-   Acceptance Criteria: The user can mark tasks as "In Progress" or "Completed," and the status will be updated in the database.
    

  

-   As a user, I want to delete tasks that are no longer needed so that my task list stays relevant.
    

	-   Acceptance Criteria: The user can delete a task, and it will be removed from the database.
## **Mockups**
**![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdycbPKUo5wwhkgxw7tD9RxuZutc_eEHrYvNPe3uzXwJ4cqoq2HpsDK7YLOAFIpVUeSfTiRwc7uCTaQfgFfmfZbFnFL5VoqJKFYdPuWxYKxxMv6-Aj8UTFq4OGgHKwu1-JQicnVD75S5-Lby9cUxg0mCgTk?key=4XbUcFGf9gSlmdzegHM0Tg)**

## Authors
- George Avong
- Mrs Onyinyechi Ikediego
