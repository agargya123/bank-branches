DROP VIEW bank_branches;
DROP TABLE branches;
DROP TABLE banks;
CREATE DATABASE bank_db;
CREATE TABLE banks (
    name character varying(49),
    id bigint NOT NULL
);

--
-- Name: branches; Type: TABLE; Schema: public; Owner: siva; Tablespace: 
--

CREATE TABLE branches (
    ifsc character varying(11) NOT NULL,
    bank_id bigint,
    branch character varying(174),
    address character varying(300),
    city character varying(50),
    district character varying(50),
    state character varying(26)
);


--
-- Name: bank_branches; Type: VIEW; Schema: public; Owner: siva
--

CREATE VIEW bank_branches AS
 SELECT branches.ifsc,
    branches.bank_id,
    branches.branch,
    branches.address,
    branches.city,
    branches.district,
    branches.state,
    banks.name AS bank_name
   FROM (branches
     JOIN banks ON ((branches.bank_id = banks.id)));
   SET CLIENT_ENCODING TO 'utf8';

   COPY banks (name, id) FROM 'G:/semester 5/bank_og.csv' CSV HEADER;

   COPY branches (ifsc, bank_id, branch, address, city, district, state) FROM 'G:/semester 5/googlebanks.csv'  CSV HEADER;
   --(DELIMITER(','))