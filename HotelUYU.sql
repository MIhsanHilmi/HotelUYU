create database hotel_uyu;

use hotel_uyu;

create table admin(
    id_admin int primary key,
    username varchar (100),
    kata_sandi varchar(255),
    nama_lengkap varchar(100)
);

create table kamar(
    no_kamar int primary key,
    jenis_kamar varchar (100) not null
);

create table reservasi(
    id_reservasi int primary key auto_increment,
    id_admin int,
    id_kamar int,
    tanggal_pemesanan date,
    nama_pemesan varchar (100) not null,
    foreign key (id_admin) references admin (id_admin),
    foreign key (id_kamar) references kamar (no_kamar)
);

insert into
    admin (id_admin, username, kata_sandi, nama_lengkap)
values
    (
        1,
        "super admin",
        MD5("superadmin1234"),
        "Albert Wayne"
    ),
    (2, "admin1", MD5("admin1111"), "Supriadi"),
    (3, "admin2", MD5("admin2222"), "Ratna Sari");

insert into
    kamar(no_kamar, jenis_kamar)
values
    (01, "Single"),
    (02, "Single"),
    (03, "Single"),
    (04, "Single"),
    (05, "Single"),
    (06, "Single"),
    (07, "Single"),
    (08, "Single"),
    (09, "Single"),
    (010, "Single"),
    (011, "Single"),
    (012, "Single"),
    (013, "Single"),
    (014, "Single"),
    (015, "Single"),
    (016, "Single"),
    (017, "Single"),
    (018, "Single"),
    (019, "Single"),
    (20, "Single"),
    (21, "Twin"),
    (22, "Twin"),
    (23, "Twin"),
    (24, "Twin"),
    (25, "Twin"),
    (26, "Twin"),
    (27, "Twin"),
    (28, "Twin"),
    (29, "Twin"),
    (30, "Twin"),
    (31, "Twin"),
    (32, "Twin"),
    (33, "Twin"),
    (34, "Twin"),
    (35, "Twin"),
    (36, "Double"),
    (37, "Double"),
    (38, "Double"),
    (39, "Double"),
    (40, "Double"),
    (41, "Family"),
    (042, "Family"),
    (043, "Family"),
    (044, "Family"),
    (045, "Family"),
    (046, "Family"),
    (047, "Family"),
    (048, "Family"),
    (049, "Family"),
    (050, "Family"),
    (51, "Deluxe"),
    (52, "Deluxe"),
    (53, "Deluxe"),
    (54, "Deluxe"),
    (55, "Deluxe"),
    (56, "Suite"),
    (57, "Suite"),
    (58, "Suite"),
    (59, "Suite"),
    (60, "Suite");