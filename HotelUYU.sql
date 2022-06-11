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
    (02, "Twin"),
    (03, "Double"),
    (04, "Family"),
    (05, "Deluxe"),
    (06, "Suite");