# Contact Manager App - py4web

This is a contact management application built with **py4web**, designed to demonstrate secure handling of user-specific contacts. Each user can create, view, edit, and delete their contacts while ensuring that they cannot access or modify contacts belonging to other users.

## Features

- **Display Contact List**: The main page displays a list of contacts with first and last names.
- **Add Contacts**: A form allows users to add new contacts, with each form signed via `_formkey` for security.
- **Edit Contacts**: Contacts can be edited, and the form is pre-filled with the contact’s information.
- **Delete Contacts**: Users can delete their own contacts, with actions signed for security.
- **User Access**: Each user can see and edit only their contacts. Attempts to tamper with edit URLs do not reveal other users' data.

## Project Structure

- **/index**: Displays the contact list for the logged-in user.
- **Add Contact**: Accessible via an "Add Contact" button. Leads to a form for adding new contacts.
- **Edit Contact**: Users can click an "Edit" button to modify their contact, with the form pre-filled with the current data.
- **Delete Contact**: Users can delete contacts using a "Delete" button.

## Security

This app employs security best practices:
- **Form Signing**: All add/edit/delete operations are protected using signed forms to ensure no unauthorized actions can be performed.
- **Data Privacy**: Users can only view and manage their own contacts. URL tampering does not expose or allow access to other users' data.

## Lessons Learned

Throughout this project, I learned how important it is to ensure data privacy and security in web applications, especially when handling user-specific data. Implementing signed forms using py4web’s built-in mechanisms provided strong protection against unauthorized data access and manipulation. Moreover, testing URL tampering helped highlight the importance of verifying user permissions at every step.

## What is py4web?

**py4web** is a Python web framework designed to be simple and lightweight while providing the necessary tools to build secure and efficient web applications. It simplifies many common tasks, such as handling user authentication, form management, and database operations, while allowing developers to focus on creating functional features with minimal overhead.
