#!/bin/bash

# Wait for MySQL to be ready
/wait-for-it.sh mysql 3306 -- echo "MySQL is up"

until curl -s -f "http://limesurvey:80" > /dev/null; do
    >&2 echo "Web service is unavailable - sleeping"
    sleep 1
done

echo "Web service is up - executing command"

# Insert the data
mysql -h mysql -u root -pexample <<EOF
USE limesurvey;

CREATE TABLE \`flag\` (
  \`flag\` text COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO \`flag\` (\`flag\`) VALUES
('WRECKIT50{aplikasiopensourceyangseringdipakeinstansiternyatamasihadasqli}');

INSERT INTO \`users\` (\`uid\`, \`users_name\`, \`password\`, \`full_name\`, \`parent_id\`, \`lang\`, \`email\`, \`htmleditormode\`, \`templateeditormode\`, \`questionselectormode\`, \`one_time_pw\`, \`dateformat\`, \`last_login\`, \`created\`, \`modified\`, \`validation_key\`, \`validation_key_expiration\`, \`last_forgot_email_password\`, \`expires\`, \`user_status\`) VALUES
(2, 'mack', '\$2y\$10\$5aHMspuGtIDx0eXzZ9KDLeZvMpzDkHbnpiI7OKwsyjLDK1oH5QBcS', 'mack', 1, 'auto', 'mack@mail.com', 'default', 'default', 'default', NULL, 1, '2024-07-20 06:35:13', '2024-07-20 04:34:15', '2024-07-20 04:35:13', NULL, NULL, NULL, NULL, 1);

INSERT INTO \`settings_user\` (\`id\`, \`uid\`, \`entity\`, \`entity_id\`, \`stg_name\`, \`stg_value\`) VALUES
(2, 2, NULL, NULL, 'showScriptEdit', '1'),
(3, 2, NULL, NULL, 'noViewMode', '0'),
(4, 2, NULL, NULL, 'answeroptionprefix', 'AO'),
(5, 2, NULL, NULL, 'subquestionprefix', 'SQ'),
(6, 2, NULL, NULL, 'lock_organizer', '0');

INSERT INTO \`permissions\` (\`id\`, \`entity\`, \`entity_id\`, \`uid\`, \`permission\`, \`create_p\`, \`read_p\`, \`update_p\`, \`delete_p\`, \`import_p\`, \`export_p\`) VALUES
(2, 'global', 0, 2, 'auth_db', 0, 1, 0, 0, 0, 0),
(3, 'template', 0, 2, 'fruity_twentythree', 0, 1, 0, 0, 0, 0),
(4, 'global', 0, 2, 'participantpanel', 0, 0, 0, 0, 0, 0),
(5, 'global', 0, 2, 'labelsets', 0, 0, 0, 0, 0, 0),
(6, 'global', 0, 2, 'settings', 0, 0, 0, 0, 0, 0),
(7, 'global', 0, 2, 'surveysgroups', 0, 0, 0, 0, 0, 0),
(8, 'global', 0, 2, 'surveys', 1, 1, 1, 1, 0, 1),
(9, 'global', 0, 2, 'templates', 0, 0, 0, 0, 0, 0),
(10, 'global', 0, 2, 'usergroups', 0, 0, 0, 0, 0, 0),
(11, 'global', 0, 2, 'users', 0, 0, 0, 0, 0, 0),
(12, 'global', 0, 2, 'superadmin', 0, 0, 0, 0, 0, 0),
(13, 'survey', 478939, 2, 'assessments', 1, 1, 1, 1, 0, 0),
(14, 'survey', 478939, 2, 'quotas', 1, 1, 1, 1, 0, 0),
(15, 'survey', 478939, 2, 'responses', 1, 1, 1, 1, 1, 1),
(16, 'survey', 478939, 2, 'statistics', 0, 1, 0, 0, 0, 0),
(17, 'survey', 478939, 2, 'survey', 0, 1, 0, 1, 0, 0),
(18, 'survey', 478939, 2, 'surveyactivation', 0, 0, 1, 0, 0, 0),
(19, 'survey', 478939, 2, 'surveycontent', 1, 1, 1, 1, 1, 1),
(20, 'survey', 478939, 2, 'surveylocale', 0, 1, 1, 0, 0, 0),
(21, 'survey', 478939, 2, 'surveysecurity', 1, 1, 1, 1, 0, 0),
(22, 'survey', 478939, 2, 'surveysettings', 0, 1, 1, 0, 0, 0),
(23, 'survey', 478939, 2, 'tokens', 1, 1, 1, 1, 1, 1),
(24, 'survey', 478939, 2, 'translations', 0, 1, 1, 0, 0, 0);
EOF
