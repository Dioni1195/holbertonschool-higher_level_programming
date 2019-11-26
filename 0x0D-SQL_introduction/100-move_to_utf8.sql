-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server.
ALTER SCHEMA hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER SCHEMA.first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER SCHEMA.first_table ALTER COLUMN name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
