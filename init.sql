
DO $$ 
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'users') THEN
        IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'users_id_seq') THEN
            CREATE SEQUENCE users_id_seq START WITH 1 INCREMENT BY 1 OWNED BY users.id;
        END IF;
    END IF;
END $$;

DO $$ 
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'potential_recruits') THEN
        IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'potential_recruits_id_seq') THEN
            CREATE SEQUENCE potential_recruits_id_seq START WITH 1 INCREMENT BY 1 OWNED BY potential_recruits.id;
        END IF;
    END IF;
END $$;

DO $$ 
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'employees') THEN
        IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'employees_id_seq') THEN
            CREATE SEQUENCE employees_id_seq START WITH 1 INCREMENT BY 1 OWNED BY employees.id;
        END IF;
    END IF;
END $$;

DO $$ 
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'events') THEN
        IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'events_id_seq') THEN
            CREATE SEQUENCE events_id_seq START WITH 1 INCREMENT BY 1 OWNED BY events.id;
        END IF;
    END IF;
END $$;

DO $$ 
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'approved_places') THEN
        IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'approved_places_id_seq') THEN
            CREATE SEQUENCE approved_places_id_seq START WITH 1 INCREMENT BY 1 OWNED BY approved_places.id;
        END IF;
    END IF;
END $$;

DO $$ 
BEGIN
    IF EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'formation_events') THEN
        IF NOT EXISTS (SELECT 1 FROM pg_class WHERE relname = 'formation_events_id_seq') THEN
            CREATE SEQUENCE formation_events_id_seq START WITH 1 INCREMENT BY 1 OWNED BY formation_events.id;
        END IF;
    END IF;
END $$;

ALTER TABLE users ALTER COLUMN id SET DEFAULT nextval('users_id_seq');
ALTER TABLE potential_recruits ALTER COLUMN id SET DEFAULT nextval('potential_recruits_id_seq');
ALTER TABLE employees ALTER COLUMN id SET DEFAULT nextval('employees_id_seq');
ALTER TABLE events ALTER COLUMN id SET DEFAULT nextval('events_id_seq');
ALTER TABLE approved_places ALTER COLUMN id SET DEFAULT nextval('approved_places_id_seq');
ALTER TABLE formation_events ALTER COLUMN id SET DEFAULT nextval('formation_events_id_seq');

SELECT pg_catalog.setval('users_id_seq', (SELECT COALESCE(MAX(id), 1) FROM users) + 1, false);
SELECT pg_catalog.setval('potential_recruits_id_seq', (SELECT COALESCE(MAX(id), 1) FROM potential_recruits) + 1, false);
SELECT pg_catalog.setval('employees_id_seq', (SELECT COALESCE(MAX(id), 1) FROM employees) + 1, false);
SELECT pg_catalog.setval('events_id_seq', (SELECT COALESCE(MAX(id), 1) FROM events) + 1, false);
SELECT pg_catalog.setval('approved_places_id_seq', (SELECT COALESCE(MAX(id), 1) FROM approved_places) + 1, false);
SELECT pg_catalog.setval('formation_events_id_seq', (SELECT COALESCE(MAX(id), 1) FROM formation_events) + 1, false);
