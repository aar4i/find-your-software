CREATE DATABASE IF NOT EXISTS find_your_software;
USE find_your_software;

CREATE TABLE IF NOT EXISTS software (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    features TEXT,
    description TEXT,
    category VARCHAR(100)
);

INSERT INTO software (name, features, description, category) VALUES
('Notion', 'docs, wiki, knowledge base, databases, kanban, tasks, templates, calendar, reminders, relations, rollups, AI notes, comments, real-time co-editing, web clipper, integrations, API, permissions, sharing', 'Notion is a productivity and organization platform', 'Productivity'),
('Jira', 'scrum boards, sprints, backlog, epics, roadmaps, bug tracking, JQL search, workflows, custom fields, automation rules, reports, velocity charts, permissions, audit log, integrations, REST API', 'Jira is a project management and issue tracking tool', 'Project Management'),
('Figma', 'vector editing, components, design system, auto layout, prototyping, smart animate, comments, real-time collaboration, developer handoff, design tokens, plugins, version history, shared libraries', 'Figma is a UI/UX design and collaboration tool', 'Design'),
('Salesforce', 'CRM, lead management, opportunities, pipeline, account management, dashboards, email sync, workflows, approvals, marketing automation, CPQ, service console, AppExchange, API, data import/export', 'Salesforce is a customer relationship management platform', 'CRM'),
('VS Code', 'code editor, debugger, integrated terminal, extensions, themes, intellisense, linting, formatting, refactoring, Git integration, remote development, devcontainers, Jupyter notebooks, REST client', 'VS Code is a code editor for developers', 'Development'),
('QuickBooks', 'invoicing, estimates/quotes, expenses, bank feeds, reconciliation, time tracking, tax/VAT, payroll (add-on), inventory (plus), purchase orders, financial reports, multi-currency, payments', 'QuickBooks is accounting software for small businesses', 'Finance'),
('Moodle', 'LMS, courses, gradebook, quiz engine, assignments, SCORM/xAPI, forums, certificates, learning paths, enrollments, analytics, question banks, badges, mobile app, plugins', 'Moodle is a learning management system', 'Education'),
('Canva', 'templates, drag-and-drop, brand kit, presentations, social posts, stock library, background remover, magic resize, animations, video editing, exports, collaboration, comments, scheduling', 'Canva is a design tool for creating visual content', 'Design'),
('Trello', 'kanban boards, checklists, due dates, labels, attachments, calendar view, timeline, table view, Butler automation, power-ups, templates, custom fields, workspace sharing, notifications', 'Trello is a task and project management tool', 'Project Management'),
('SAP ERP', 'general ledger, accounts payable/receivable, procurement, inventory, MRP, production planning, HR, payroll, compliance, audit, analytics, integrations, multi-entity, workflows, localization', 'SAP ERP is enterprise resource planning software', 'ERP'),
('Asana', 'tasks, subtasks, dependencies, timeline (Gantt), goals/OKRs, portfolios, workload, forms/intake, automation, rules, templates, approvals, dashboards, custom fields, integrations', 'Asana is a task and project management tool', 'Project Management'),
('Adobe XD', 'wireframing, UI design, components, states/variants, prototyping, interactions, voice prototyping, co-editing, comments, design specs, developer handoff, asset export, plugins', 'Adobe XD is a UI/UX design tool', 'Design'),
('GitHub', 'repositories, issues, pull requests, code review, actions (CI/CD), packages, environments, wiki, projects (boards), discussions, security scanning, dependabot, pages, REST/GraphQL APIs', 'GitHub is a platform for hosting and collaborating on code', 'Development'),
('FreshBooks', 'invoicing, estimates, proposals, time tracking, expenses, mileage, client portal, online payments, late fees, retainers, recurring invoices, reports, tax summaries', 'FreshBooks is accounting and invoicing software', 'Finance'),
('Zoom', 'video meetings, webinars, chat, screen sharing, breakout rooms, whiteboard, recording, cloud storage, transcription, waiting room, polls, Q&A, calendar integration, virtual backgrounds', 'Zoom is a video communication platform', 'Communication');
