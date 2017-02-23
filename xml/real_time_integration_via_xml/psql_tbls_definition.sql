-- Table: temp_insurance2_ebureau_realtime_t
-- DROP TABLE temp_insurance2_ebureau_realtime_t;

CREATE TABLE temp_insurance2_ebureau_realtime_t
(
  payload xml
)
WITH (
  OIDS=FALSE
);


-- Table: insurance2_ebureau_addr_t
-- DROP TABLE insurance2_ebureau_addr_t;

CREATE TABLE insurance2_ebureau_addr_t
(
  id integer NOT NULL DEFAULT nextval('insurance2_ebureau_addr_id_seq'::regclass),
  cust_id numeric(4,0) NOT NULL,
  our_run_date timestamp without time zone NOT NULL,
  seqnum integer NOT NULL,
  eb_addr_fname character varying(30),
  eb_addr_lname character varying(30),
  eb_addr_addr1 character varying(50),
  eb_addr_city character varying(30),
  eb_addr_state character varying(2),
  eb_addr_zip5 character varying(5),
  eb_addr_zip4 character varying(4),
  eb_addr_dob character varying(6),
  eb_addr_match character varying(5),
  eb_addr_status character varying(4),
  eb_addr_score integer,
  eb_addr_rank integer,
  CONSTRAINT insurance2_ebureau_addr_t_pkey PRIMARY KEY (id),
  CONSTRAINT insurance2_ebureau_addr_t_cust_id_check CHECK (cust_id >= 1::numeric AND cust_id <= 9999::numeric)
)
WITH (
  OIDS=FALSE
);

-- Table: insurance2_ebureau_error_t
-- DROP TABLE insurance2_ebureau_error_t;

CREATE TABLE insurance2_ebureau_error_t
(
  id integer NOT NULL DEFAULT nextval('insurance2_ebureau_error_id_seq'::regclass),
  cust_id numeric(4,0) NOT NULL,
  our_run_date timestamp without time zone NOT NULL,
  seqnum integer NOT NULL,
  eb_error_message character varying(75),
  CONSTRAINT insurance2_ebureau_error_t_pkey PRIMARY KEY (id),
  CONSTRAINT insurance2_ebureau_error_t_cust_id_check CHECK (cust_id >= 1::numeric AND cust_id <= 9999::numeric)
)
WITH (
  OIDS=FALSE
);

-- Table: insurance2_ebureau_message_t
-- DROP TABLE insurance2_ebureau_message_t;

CREATE TABLE insurance2_ebureau_message_t
(
  id integer NOT NULL DEFAULT nextval('insurance2_ebureau_message_id_seq'::regclass),
  cust_id numeric(4,0) NOT NULL,
  our_run_date timestamp without time zone NOT NULL,
  seqnum integer NOT NULL,
  eb_message character varying(75),
  CONSTRAINT insurance2_ebureau_message_t_pkey PRIMARY KEY (id),
  CONSTRAINT insurance2_ebureau_message_t_cust_id_check CHECK (cust_id >= 1::numeric AND cust_id <= 9999::numeric)
)
WITH (
  OIDS=FALSE
);