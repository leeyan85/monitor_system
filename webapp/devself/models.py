# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Acknowledges(models.Model):
    acknowledgeid = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Users', db_column='userid')
    eventid = models.ForeignKey('Events', db_column='eventid')
    clock = models.IntegerField()
    message = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'acknowledges'


class Actions(models.Model):
    actionid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    eventsource = models.IntegerField()
    evaltype = models.IntegerField()
    status = models.IntegerField()
    esc_period = models.IntegerField()
    def_shortdata = models.CharField(max_length=255)
    def_longdata = models.TextField()
    recovery_msg = models.IntegerField()
    r_shortdata = models.CharField(max_length=255)
    r_longdata = models.TextField()
    formula = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'actions'


class Alerts(models.Model):
    alertid = models.BigIntegerField(primary_key=True)
    actionid = models.ForeignKey(Actions, db_column='actionid')
    eventid = models.ForeignKey('Events', db_column='eventid')
    userid = models.ForeignKey('Users', db_column='userid', blank=True, null=True)
    clock = models.IntegerField()
    mediatypeid = models.ForeignKey('MediaType', db_column='mediatypeid', blank=True, null=True)
    sendto = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.IntegerField()
    retries = models.IntegerField()
    error = models.CharField(max_length=128)
    esc_step = models.IntegerField()
    alerttype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alerts'


class ApplicationDiscovery(models.Model):
    application_discoveryid = models.BigIntegerField(primary_key=True)
    applicationid = models.ForeignKey('Applications', db_column='applicationid')
    application_prototypeid = models.ForeignKey('ApplicationPrototype', db_column='application_prototypeid')
    name = models.CharField(max_length=255)
    lastcheck = models.IntegerField()
    ts_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'application_discovery'


class ApplicationPrototype(models.Model):
    application_prototypeid = models.BigIntegerField(primary_key=True)
    itemid = models.ForeignKey('Items', db_column='itemid')
    templateid = models.ForeignKey('self', db_column='templateid', blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'application_prototype'




class Applications(models.Model):
    applicationid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey('Hosts', db_column='hostid')
    name = models.CharField(max_length=255)
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'applications'
        unique_together = (('hostid', 'name'),)


class Auditlog(models.Model):
    auditid = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Users', db_column='userid')
    clock = models.IntegerField()
    action = models.IntegerField()
    resourcetype = models.IntegerField()
    details = models.CharField(max_length=128)
    ip = models.CharField(max_length=39)
    resourceid = models.BigIntegerField()
    resourcename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auditlog'


class AuditlogDetails(models.Model):
    auditdetailid = models.BigIntegerField(primary_key=True)
    auditid = models.ForeignKey(Auditlog, db_column='auditid')
    table_name = models.CharField(max_length=64)
    field_name = models.CharField(max_length=64)
    oldvalue = models.TextField()
    newvalue = models.TextField()

    class Meta:
        managed = False
        db_table = 'auditlog_details'


class AutoregHost(models.Model):
    autoreg_hostid = models.BigIntegerField(primary_key=True)
    proxy_hostid = models.ForeignKey('Hosts', db_column='proxy_hostid', blank=True, null=True)
    host = models.CharField(max_length=64)
    listen_ip = models.CharField(max_length=39)
    listen_port = models.IntegerField()
    listen_dns = models.CharField(max_length=64)
    host_metadata = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'autoreg_host'


class Conditions(models.Model):
    conditionid = models.BigIntegerField(primary_key=True)
    actionid = models.ForeignKey(Actions, db_column='actionid')
    conditiontype = models.IntegerField()
    operator = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'conditions'


class Config(models.Model):
    configid = models.BigIntegerField(primary_key=True)
    refresh_unsupported = models.IntegerField()
    work_period = models.CharField(max_length=100)
    alert_usrgrpid = models.ForeignKey('Usrgrp', db_column='alert_usrgrpid', blank=True, null=True)
    event_ack_enable = models.IntegerField()
    event_expire = models.IntegerField()
    event_show_max = models.IntegerField()
    default_theme = models.CharField(max_length=128)
    authentication_type = models.IntegerField()
    ldap_host = models.CharField(max_length=255)
    ldap_port = models.IntegerField()
    ldap_base_dn = models.CharField(max_length=255)
    ldap_bind_dn = models.CharField(max_length=255)
    ldap_bind_password = models.CharField(max_length=128)
    ldap_search_attribute = models.CharField(max_length=128)
    dropdown_first_entry = models.IntegerField()
    dropdown_first_remember = models.IntegerField()
    discovery_groupid = models.ForeignKey('Groups', db_column='discovery_groupid')
    max_in_table = models.IntegerField()
    search_limit = models.IntegerField()
    severity_color_0 = models.CharField(max_length=6)
    severity_color_1 = models.CharField(max_length=6)
    severity_color_2 = models.CharField(max_length=6)
    severity_color_3 = models.CharField(max_length=6)
    severity_color_4 = models.CharField(max_length=6)
    severity_color_5 = models.CharField(max_length=6)
    severity_name_0 = models.CharField(max_length=32)
    severity_name_1 = models.CharField(max_length=32)
    severity_name_2 = models.CharField(max_length=32)
    severity_name_3 = models.CharField(max_length=32)
    severity_name_4 = models.CharField(max_length=32)
    severity_name_5 = models.CharField(max_length=32)
    ok_period = models.IntegerField()
    blink_period = models.IntegerField()
    problem_unack_color = models.CharField(max_length=6)
    problem_ack_color = models.CharField(max_length=6)
    ok_unack_color = models.CharField(max_length=6)
    ok_ack_color = models.CharField(max_length=6)
    problem_unack_style = models.IntegerField()
    problem_ack_style = models.IntegerField()
    ok_unack_style = models.IntegerField()
    ok_ack_style = models.IntegerField()
    snmptrap_logging = models.IntegerField()
    server_check_interval = models.IntegerField()
    hk_events_mode = models.IntegerField()
    hk_events_trigger = models.IntegerField()
    hk_events_internal = models.IntegerField()
    hk_events_discovery = models.IntegerField()
    hk_events_autoreg = models.IntegerField()
    hk_services_mode = models.IntegerField()
    hk_services = models.IntegerField()
    hk_audit_mode = models.IntegerField()
    hk_audit = models.IntegerField()
    hk_sessions_mode = models.IntegerField()
    hk_sessions = models.IntegerField()
    hk_history_mode = models.IntegerField()
    hk_history_global = models.IntegerField()
    hk_history = models.IntegerField()
    hk_trends_mode = models.IntegerField()
    hk_trends_global = models.IntegerField()
    hk_trends = models.IntegerField()
    default_inventory_mode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'config'


class Dbversion(models.Model):
    mandatory = models.IntegerField()
    optional = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dbversion'


class Dchecks(models.Model):
    dcheckid = models.BigIntegerField(primary_key=True)
    druleid = models.ForeignKey('Drules', db_column='druleid')
    type = models.IntegerField()
    key_field = models.CharField(db_column='key_', max_length=255)  # Field renamed because it ended with '_'.
    snmp_community = models.CharField(max_length=255)
    ports = models.CharField(max_length=255)
    snmpv3_securityname = models.CharField(max_length=64)
    snmpv3_securitylevel = models.IntegerField()
    snmpv3_authpassphrase = models.CharField(max_length=64)
    snmpv3_privpassphrase = models.CharField(max_length=64)
    uniq = models.IntegerField()
    snmpv3_authprotocol = models.IntegerField()
    snmpv3_privprotocol = models.IntegerField()
    snmpv3_contextname = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dchecks'


class Dhosts(models.Model):
    dhostid = models.BigIntegerField(primary_key=True)
    druleid = models.ForeignKey('Drules', db_column='druleid')
    status = models.IntegerField()
    lastup = models.IntegerField()
    lastdown = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dhosts'


class Drules(models.Model):
    druleid = models.BigIntegerField(primary_key=True)
    proxy_hostid = models.ForeignKey('Hosts', db_column='proxy_hostid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    iprange = models.CharField(max_length=2048)
    delay = models.IntegerField()
    nextcheck = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drules'




class Escalations(models.Model):
    escalationid = models.BigIntegerField(primary_key=True)
    actionid = models.BigIntegerField()
    triggerid = models.BigIntegerField(blank=True, null=True)
    eventid = models.BigIntegerField(blank=True, null=True)
    r_eventid = models.BigIntegerField(blank=True, null=True)
    nextcheck = models.IntegerField()
    esc_step = models.IntegerField()
    status = models.IntegerField()
    itemid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'escalations'
        unique_together = (('actionid', 'triggerid', 'itemid', 'escalationid'),)


class Events(models.Model):
    eventid = models.BigIntegerField(primary_key=True)
    source = models.IntegerField()
    object = models.IntegerField()
    objectid = models.BigIntegerField()
    clock = models.IntegerField()
    value = models.IntegerField()
    acknowledged = models.IntegerField()
    ns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'events'


class Expressions(models.Model):
    expressionid = models.BigIntegerField(primary_key=True)
    regexpid = models.ForeignKey('Regexps', db_column='regexpid')
    expression = models.CharField(max_length=255)
    expression_type = models.IntegerField()
    exp_delimiter = models.CharField(max_length=1)
    case_sensitive = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'expressions'


class Functions(models.Model):
    functionid = models.BigIntegerField(primary_key=True)
    itemid = models.ForeignKey('Items', db_column='itemid')
    triggerid = models.ForeignKey('Triggers', db_column='triggerid')
    function = models.CharField(max_length=12)
    parameter = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'functions'


class Globalmacro(models.Model):
    globalmacroid = models.BigIntegerField(primary_key=True)
    macro = models.CharField(unique=True, max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'globalmacro'


class Globalvars(models.Model):
    globalvarid = models.BigIntegerField(primary_key=True)
    snmp_lastsize = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'globalvars'



class GraphTheme(models.Model):
    graphthemeid = models.BigIntegerField(primary_key=True)
    theme = models.CharField(unique=True, max_length=64)
    backgroundcolor = models.CharField(max_length=6)
    graphcolor = models.CharField(max_length=6)
    gridcolor = models.CharField(max_length=6)
    maingridcolor = models.CharField(max_length=6)
    gridbordercolor = models.CharField(max_length=6)
    textcolor = models.CharField(max_length=6)
    highlightcolor = models.CharField(max_length=6)
    leftpercentilecolor = models.CharField(max_length=6)
    rightpercentilecolor = models.CharField(max_length=6)
    nonworktimecolor = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'graph_theme'




class GroupDiscovery(models.Model):
    groupid = models.OneToOneField('Groups', db_column='groupid', primary_key=True)
    parent_group_prototypeid = models.ForeignKey('GroupPrototype', db_column='parent_group_prototypeid')
    name = models.CharField(max_length=64)
    lastcheck = models.IntegerField()
    ts_delete = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'group_discovery'


class GroupPrototype(models.Model):
    group_prototypeid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey('Hosts', db_column='hostid')
    name = models.CharField(max_length=64)
    groupid = models.ForeignKey('Groups', db_column='groupid', blank=True, null=True)
    templateid = models.ForeignKey('self', db_column='templateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'group_prototype'


class Groups(models.Model):
    groupid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    internal = models.IntegerField()
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups'


class History(models.Model):
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    value = models.FloatField()
    ns = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'history'


class HistoryLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    timestamp = models.IntegerField()
    source = models.CharField(max_length=64)
    severity = models.IntegerField()
    value = models.TextField()
    logeventid = models.IntegerField()
    ns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history_log'
        unique_together = (('itemid', 'id'),)


class HistoryStr(models.Model):
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    value = models.CharField(max_length=255)
    ns = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'history_str'


class HistoryText(models.Model):
    id = models.BigIntegerField(primary_key=True)
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    value = models.TextField()
    ns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'history_text'
        unique_together = (('itemid', 'id'),)


class HistoryUint(models.Model):
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    value = models.BigIntegerField()
    ns = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'history_uint'




class HostInventory(models.Model):
    hostid = models.OneToOneField('Hosts', db_column='hostid', primary_key=True)
    inventory_mode = models.IntegerField()
    type = models.CharField(max_length=64)
    type_full = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    alias = models.CharField(max_length=64)
    os = models.CharField(max_length=64)
    os_full = models.CharField(max_length=255)
    os_short = models.CharField(max_length=64)
    serialno_a = models.CharField(max_length=64)
    serialno_b = models.CharField(max_length=64)
    tag = models.CharField(max_length=64)
    asset_tag = models.CharField(max_length=64)
    macaddress_a = models.CharField(max_length=64)
    macaddress_b = models.CharField(max_length=64)
    hardware = models.CharField(max_length=255)
    hardware_full = models.TextField()
    software = models.CharField(max_length=255)
    software_full = models.TextField()
    software_app_a = models.CharField(max_length=64)
    software_app_b = models.CharField(max_length=64)
    software_app_c = models.CharField(max_length=64)
    software_app_d = models.CharField(max_length=64)
    software_app_e = models.CharField(max_length=64)
    contact = models.TextField()
    location = models.TextField()
    location_lat = models.CharField(max_length=16)
    location_lon = models.CharField(max_length=16)
    notes = models.TextField()
    chassis = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    hw_arch = models.CharField(max_length=32)
    vendor = models.CharField(max_length=64)
    contract_number = models.CharField(max_length=64)
    installer_name = models.CharField(max_length=64)
    deployment_status = models.CharField(max_length=64)
    url_a = models.CharField(max_length=255)
    url_b = models.CharField(max_length=255)
    url_c = models.CharField(max_length=255)
    host_networks = models.TextField()
    host_netmask = models.CharField(max_length=39)
    host_router = models.CharField(max_length=39)
    oob_ip = models.CharField(max_length=39)
    oob_netmask = models.CharField(max_length=39)
    oob_router = models.CharField(max_length=39)
    date_hw_purchase = models.CharField(max_length=64)
    date_hw_install = models.CharField(max_length=64)
    date_hw_expiry = models.CharField(max_length=64)
    date_hw_decomm = models.CharField(max_length=64)
    site_address_a = models.CharField(max_length=128)
    site_address_b = models.CharField(max_length=128)
    site_address_c = models.CharField(max_length=128)
    site_city = models.CharField(max_length=128)
    site_state = models.CharField(max_length=64)
    site_country = models.CharField(max_length=64)
    site_zip = models.CharField(max_length=64)
    site_rack = models.CharField(max_length=128)
    site_notes = models.TextField()
    poc_1_name = models.CharField(max_length=128)
    poc_1_email = models.CharField(max_length=128)
    poc_1_phone_a = models.CharField(max_length=64)
    poc_1_phone_b = models.CharField(max_length=64)
    poc_1_cell = models.CharField(max_length=64)
    poc_1_screen = models.CharField(max_length=64)
    poc_1_notes = models.TextField()
    poc_2_name = models.CharField(max_length=128)
    poc_2_email = models.CharField(max_length=128)
    poc_2_phone_a = models.CharField(max_length=64)
    poc_2_phone_b = models.CharField(max_length=64)
    poc_2_cell = models.CharField(max_length=64)
    poc_2_screen = models.CharField(max_length=64)
    poc_2_notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'host_inventory'


class Hostmacro(models.Model):
    hostmacroid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey('Hosts', db_column='hostid')
    macro = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'hostmacro'
        unique_together = (('hostid', 'macro'),)


class Hosts(models.Model):
    hostid = models.BigIntegerField(primary_key=True)
    host = models.CharField(max_length=128)
    status = models.IntegerField()
    disable_until = models.IntegerField()
    error = models.CharField(max_length=2048)
    available = models.IntegerField()
    errors_from = models.IntegerField()
    lastaccess = models.IntegerField()
    ipmi_authtype = models.IntegerField()
    ipmi_privilege = models.IntegerField()
    ipmi_username = models.CharField(max_length=16)
    ipmi_password = models.CharField(max_length=20)
    ipmi_disable_until = models.IntegerField()
    ipmi_available = models.IntegerField()
    snmp_disable_until = models.IntegerField()
    snmp_available = models.IntegerField()
    maintenanceid = models.ForeignKey('Maintenances', db_column='maintenanceid', blank=True, null=True)
    maintenance_status = models.IntegerField()
    maintenance_type = models.IntegerField()
    maintenance_from = models.IntegerField()
    ipmi_errors_from = models.IntegerField()
    snmp_errors_from = models.IntegerField()
    ipmi_error = models.CharField(max_length=2048)
    snmp_error = models.CharField(max_length=2048)
    jmx_disable_until = models.IntegerField()
    jmx_available = models.IntegerField()
    jmx_errors_from = models.IntegerField()
    jmx_error = models.CharField(max_length=2048)
    name = models.CharField(max_length=128)
    flags = models.IntegerField()
    templateid = models.ForeignKey('self', db_column='templateid', blank=True, null=True)
    description = models.TextField()
    tls_connect = models.IntegerField()
    tls_accept = models.IntegerField()
    tls_issuer = models.CharField(max_length=1024)
    tls_subject = models.CharField(max_length=1024)
    tls_psk_identity = models.CharField(max_length=128)
    tls_psk = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'hosts'


class HostsGroups(models.Model):
    hostgroupid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey(Hosts, db_column='hostid')
    groupid = models.ForeignKey(Groups, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'hosts_groups'
        unique_together = (('hostid', 'groupid'),)




class Housekeeper(models.Model):
    housekeeperid = models.BigIntegerField(primary_key=True)
    tablename = models.CharField(max_length=64)
    field = models.CharField(max_length=64)
    value = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'housekeeper'


class Httpstep(models.Model):
    httpstepid = models.BigIntegerField(primary_key=True)
    httptestid = models.ForeignKey('Httptest', db_column='httptestid')
    name = models.CharField(max_length=64)
    no = models.IntegerField()
    url = models.CharField(max_length=2048)
    timeout = models.IntegerField()
    posts = models.TextField()
    required = models.CharField(max_length=255)
    status_codes = models.CharField(max_length=255)
    variables = models.TextField()
    follow_redirects = models.IntegerField()
    retrieve_mode = models.IntegerField()
    headers = models.TextField()

    class Meta:
        managed = False
        db_table = 'httpstep'


class Httpstepitem(models.Model):
    httpstepitemid = models.BigIntegerField(primary_key=True)
    httpstepid = models.ForeignKey(Httpstep, db_column='httpstepid')
    itemid = models.ForeignKey('Items', db_column='itemid')
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'httpstepitem'
        unique_together = (('httpstepid', 'itemid'),)


class Httptest(models.Model):
    httptestid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    applicationid = models.ForeignKey(Applications, db_column='applicationid', blank=True, null=True)
    nextcheck = models.IntegerField()
    delay = models.IntegerField()
    status = models.IntegerField()
    variables = models.TextField()
    agent = models.CharField(max_length=255)
    authentication = models.IntegerField()
    http_user = models.CharField(max_length=64)
    http_password = models.CharField(max_length=64)
    hostid = models.ForeignKey(Hosts, db_column='hostid')
    templateid = models.ForeignKey('self', db_column='templateid', blank=True, null=True)
    http_proxy = models.CharField(max_length=255)
    retries = models.IntegerField()
    ssl_cert_file = models.CharField(max_length=255)
    ssl_key_file = models.CharField(max_length=255)
    ssl_key_password = models.CharField(max_length=64)
    verify_peer = models.IntegerField()
    verify_host = models.IntegerField()
    headers = models.TextField()

    class Meta:
        managed = False
        db_table = 'httptest'
        unique_together = (('hostid', 'name'),)


class Httptestitem(models.Model):
    httptestitemid = models.BigIntegerField(primary_key=True)
    httptestid = models.ForeignKey(Httptest, db_column='httptestid')
    itemid = models.ForeignKey('Items', db_column='itemid')
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'httptestitem'
        unique_together = (('httptestid', 'itemid'),)


class IconMap(models.Model):
    iconmapid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    default_iconid = models.ForeignKey('Images', db_column='default_iconid')

    class Meta:
        managed = False
        db_table = 'icon_map'


class IconMapping(models.Model):
    iconmappingid = models.BigIntegerField(primary_key=True)
    iconmapid = models.ForeignKey(IconMap, db_column='iconmapid')
    iconid = models.ForeignKey('Images', db_column='iconid')
    inventory_link = models.IntegerField()
    expression = models.CharField(max_length=64)
    sortorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'icon_mapping'


class Ids(models.Model):
    table_name = models.CharField(max_length=64)
    field_name = models.CharField(max_length=64)
    nextid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'ids'
        unique_together = (('table_name', 'field_name'),)


class Images(models.Model):
    imageid = models.BigIntegerField(primary_key=True)
    imagetype = models.IntegerField()
    name = models.CharField(unique=True, max_length=64)
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'images'


class Interface(models.Model):
    interfaceid = models.BigIntegerField(primary_key=True)
    hostid = models.ForeignKey(Hosts, db_column='hostid')
    main = models.IntegerField()
    type = models.IntegerField()
    useip = models.IntegerField()
    ip = models.CharField(max_length=64)
    dns = models.CharField(max_length=64)
    port = models.CharField(max_length=64)
    bulk = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'interface'


class ItemApplicationPrototype(models.Model):
    item_application_prototypeid = models.BigIntegerField(primary_key=True)
    application_prototypeid = models.ForeignKey(ApplicationPrototype, db_column='application_prototypeid')
    itemid = models.ForeignKey('Items', db_column='itemid')

    class Meta:
        managed = False
        db_table = 'item_application_prototype'
        unique_together = (('application_prototypeid', 'itemid'),)


class ItemCondition(models.Model):
    item_conditionid = models.BigIntegerField(primary_key=True)
    itemid = models.ForeignKey('Items', db_column='itemid')
    operator = models.IntegerField()
    macro = models.CharField(max_length=64)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'item_condition'




class Items(models.Model):
    itemid = models.BigIntegerField(primary_key=True)
    type = models.IntegerField()
    snmp_community = models.CharField(max_length=64)
    snmp_oid = models.CharField(max_length=255)
    hostid = models.ForeignKey(Hosts, db_column='hostid')
    name = models.CharField(max_length=255)
    key_field = models.CharField(db_column='key_', max_length=255)  # Field renamed because it ended with '_'.
    delay = models.IntegerField()
    history = models.IntegerField()
    trends = models.IntegerField()
    status = models.IntegerField()
    value_type = models.IntegerField()
    trapper_hosts = models.CharField(max_length=255)
    units = models.CharField(max_length=255)
    multiplier = models.IntegerField()
    delta = models.IntegerField()
    snmpv3_securityname = models.CharField(max_length=64)
    snmpv3_securitylevel = models.IntegerField()
    snmpv3_authpassphrase = models.CharField(max_length=64)
    snmpv3_privpassphrase = models.CharField(max_length=64)
    formula = models.CharField(max_length=255)
    error = models.CharField(max_length=2048)
    lastlogsize = models.BigIntegerField()
    logtimefmt = models.CharField(max_length=64)
    templateid = models.ForeignKey('self', db_column='templateid', blank=True, null=True)
    valuemapid = models.ForeignKey('Valuemaps', db_column='valuemapid', blank=True, null=True)
    delay_flex = models.CharField(max_length=255)
    params = models.TextField()
    ipmi_sensor = models.CharField(max_length=128)
    data_type = models.IntegerField()
    authtype = models.IntegerField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    publickey = models.CharField(max_length=64)
    privatekey = models.CharField(max_length=64)
    mtime = models.IntegerField()
    flags = models.IntegerField()
    interfaceid = models.ForeignKey(Interface, db_column='interfaceid', blank=True, null=True)
    port = models.CharField(max_length=64)
    description = models.TextField()
    inventory_link = models.IntegerField()
    lifetime = models.CharField(max_length=64)
    snmpv3_authprotocol = models.IntegerField()
    snmpv3_privprotocol = models.IntegerField()
    state = models.IntegerField()
    snmpv3_contextname = models.CharField(max_length=255)
    evaltype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'items'
        #unique_together = (('hostid', 'key_'),)


class ItemsApplications(models.Model):
    itemappid = models.BigIntegerField(primary_key=True)
    applicationid = models.ForeignKey(Applications, db_column='applicationid')
    itemid = models.ForeignKey(Items, db_column='itemid')

    class Meta:
        managed = False
        db_table = 'items_applications'
        unique_together = (('applicationid', 'itemid'),)


class Maintenances(models.Model):
    maintenanceid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    maintenance_type = models.IntegerField()
    description = models.TextField()
    active_since = models.IntegerField()
    active_till = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'maintenances'


class MaintenancesGroups(models.Model):
    maintenance_groupid = models.BigIntegerField(primary_key=True)
    maintenanceid = models.ForeignKey(Maintenances, db_column='maintenanceid')
    groupid = models.ForeignKey(Groups, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'maintenances_groups'
        unique_together = (('maintenanceid', 'groupid'),)


class MaintenancesHosts(models.Model):
    maintenance_hostid = models.BigIntegerField(primary_key=True)
    maintenanceid = models.ForeignKey(Maintenances, db_column='maintenanceid')
    hostid = models.ForeignKey(Hosts, db_column='hostid')

    class Meta:
        managed = False
        db_table = 'maintenances_hosts'
        unique_together = (('maintenanceid', 'hostid'),)


class MaintenancesWindows(models.Model):
    maintenance_timeperiodid = models.BigIntegerField(primary_key=True)
    maintenanceid = models.ForeignKey(Maintenances, db_column='maintenanceid')
    timeperiodid = models.ForeignKey('Timeperiods', db_column='timeperiodid')

    class Meta:
        managed = False
        db_table = 'maintenances_windows'
        unique_together = (('maintenanceid', 'timeperiodid'),)


class Mappings(models.Model):
    mappingid = models.BigIntegerField(primary_key=True)
    valuemapid = models.ForeignKey('Valuemaps', db_column='valuemapid')
    value = models.CharField(max_length=64)
    newvalue = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'mappings'


class Media(models.Model):
    mediaid = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Users', db_column='userid')
    mediatypeid = models.ForeignKey('MediaType', db_column='mediatypeid')
    sendto = models.CharField(max_length=100)
    active = models.IntegerField()
    severity = models.IntegerField()
    period = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'media'


class MediaType(models.Model):
    mediatypeid = models.BigIntegerField(primary_key=True)
    type = models.IntegerField()
    description = models.CharField(unique=True, max_length=100)
    smtp_server = models.CharField(max_length=255)
    smtp_helo = models.CharField(max_length=255)
    smtp_email = models.CharField(max_length=255)
    exec_path = models.CharField(max_length=255)
    gsm_modem = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    status = models.IntegerField()
    smtp_port = models.IntegerField()
    smtp_security = models.IntegerField()
    smtp_verify_peer = models.IntegerField()
    smtp_verify_host = models.IntegerField()
    smtp_authentication = models.IntegerField()
    exec_params = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'media_type'


class Opcommand(models.Model):
    operationid = models.OneToOneField('Operations', db_column='operationid', primary_key=True)
    type = models.IntegerField()
    scriptid = models.ForeignKey('Scripts', db_column='scriptid', blank=True, null=True)
    execute_on = models.IntegerField()
    port = models.CharField(max_length=64)
    authtype = models.IntegerField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    publickey = models.CharField(max_length=64)
    privatekey = models.CharField(max_length=64)
    command = models.TextField()

    class Meta:
        managed = False
        db_table = 'opcommand'


class OpcommandGrp(models.Model):
    opcommand_grpid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey('Operations', db_column='operationid')
    groupid = models.ForeignKey(Groups, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'opcommand_grp'


class OpcommandHst(models.Model):
    opcommand_hstid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey('Operations', db_column='operationid')
    hostid = models.ForeignKey(Hosts, db_column='hostid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opcommand_hst'


class Opconditions(models.Model):
    opconditionid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey('Operations', db_column='operationid')
    conditiontype = models.IntegerField()
    operator = models.IntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'opconditions'


class Operations(models.Model):
    operationid = models.BigIntegerField(primary_key=True)
    actionid = models.ForeignKey(Actions, db_column='actionid')
    operationtype = models.IntegerField()
    esc_period = models.IntegerField()
    esc_step_from = models.IntegerField()
    esc_step_to = models.IntegerField()
    evaltype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'operations'


class Opgroup(models.Model):
    opgroupid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey(Operations, db_column='operationid')
    groupid = models.ForeignKey(Groups, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'opgroup'
        unique_together = (('operationid', 'groupid'),)


class Opinventory(models.Model):
    operationid = models.OneToOneField(Operations, db_column='operationid', primary_key=True)
    inventory_mode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'opinventory'


class Opmessage(models.Model):
    operationid = models.OneToOneField(Operations, db_column='operationid', primary_key=True)
    default_msg = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    mediatypeid = models.ForeignKey(MediaType, db_column='mediatypeid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'opmessage'


class OpmessageGrp(models.Model):
    opmessage_grpid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey(Operations, db_column='operationid')
    usrgrpid = models.ForeignKey('Usrgrp', db_column='usrgrpid')

    class Meta:
        managed = False
        db_table = 'opmessage_grp'
        unique_together = (('operationid', 'usrgrpid'),)


class OpmessageUsr(models.Model):
    opmessage_usrid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey(Operations, db_column='operationid')
    userid = models.ForeignKey('Users', db_column='userid')

    class Meta:
        managed = False
        db_table = 'opmessage_usr'
        unique_together = (('operationid', 'userid'),)


class Optemplate(models.Model):
    optemplateid = models.BigIntegerField(primary_key=True)
    operationid = models.ForeignKey(Operations, db_column='operationid')
    templateid = models.ForeignKey(Hosts, db_column='templateid')

    class Meta:
        managed = False
        db_table = 'optemplate'
        unique_together = (('operationid', 'templateid'),)


class Profiles(models.Model):
    profileid = models.BigIntegerField(primary_key=True)
    userid = models.ForeignKey('Users', db_column='userid')
    idx = models.CharField(max_length=96)
    idx2 = models.BigIntegerField()
    value_id = models.BigIntegerField()
    value_int = models.IntegerField()
    value_str = models.CharField(max_length=255)
    source = models.CharField(max_length=96)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'profiles'


class ProxyAutoregHost(models.Model):
    id = models.BigIntegerField(primary_key=True)
    clock = models.IntegerField()
    host = models.CharField(max_length=64)
    listen_ip = models.CharField(max_length=39)
    listen_port = models.IntegerField()
    listen_dns = models.CharField(max_length=64)
    host_metadata = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'proxy_autoreg_host'


class ProxyDhistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    clock = models.IntegerField()
    druleid = models.BigIntegerField()
    type = models.IntegerField()
    ip = models.CharField(max_length=39)
    port = models.IntegerField()
    key_field = models.CharField(db_column='key_', max_length=255)  # Field renamed because it ended with '_'.
    value = models.CharField(max_length=255)
    status = models.IntegerField()
    dcheckid = models.BigIntegerField(blank=True, null=True)
    dns = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'proxy_dhistory'


class ProxyHistory(models.Model):
    id = models.BigIntegerField(primary_key=True)
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    timestamp = models.IntegerField()
    source = models.CharField(max_length=64)
    severity = models.IntegerField()
    value = models.TextField()
    logeventid = models.IntegerField()
    ns = models.IntegerField()
    state = models.IntegerField()
    lastlogsize = models.BigIntegerField()
    mtime = models.IntegerField()
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'proxy_history'


class Regexps(models.Model):
    regexpid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    test_string = models.TextField()

    class Meta:
        managed = False
        db_table = 'regexps'


class Rights(models.Model):
    rightid = models.BigIntegerField(primary_key=True)
    groupid = models.ForeignKey('Usrgrp', db_column='groupid')
    permission = models.IntegerField()
    id = models.ForeignKey(Groups, db_column='id')

    class Meta:
        managed = False
        db_table = 'rights'


class ScreenUser(models.Model):
    screenuserid = models.BigIntegerField(primary_key=True)
    screenid = models.ForeignKey('Screens', db_column='screenid')
    userid = models.ForeignKey('Users', db_column='userid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'screen_user'
        unique_together = (('screenid', 'userid'),)


class ScreenUsrgrp(models.Model):
    screenusrgrpid = models.BigIntegerField(primary_key=True)
    screenid = models.ForeignKey('Screens', db_column='screenid')
    usrgrpid = models.ForeignKey('Usrgrp', db_column='usrgrpid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'screen_usrgrp'
        unique_together = (('screenid', 'usrgrpid'),)


class Screens(models.Model):
    screenid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    hsize = models.IntegerField()
    vsize = models.IntegerField()
    templateid = models.ForeignKey(Hosts, db_column='templateid', blank=True, null=True)
    userid = models.ForeignKey('Users', db_column='userid', blank=True, null=True)
    private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'screens'


class ScreensItems(models.Model):
    screenitemid = models.BigIntegerField(primary_key=True)
    screenid = models.ForeignKey(Screens, db_column='screenid')
    resourcetype = models.IntegerField()
    resourceid = models.BigIntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    colspan = models.IntegerField()
    rowspan = models.IntegerField()
    elements = models.IntegerField()
    valign = models.IntegerField()
    halign = models.IntegerField()
    style = models.IntegerField()
    url = models.CharField(max_length=255)
    dynamic = models.IntegerField()
    sort_triggers = models.IntegerField()
    application = models.CharField(max_length=255)
    max_columns = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'screens_items'


class Scripts(models.Model):
    scriptid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    command = models.CharField(max_length=255)
    host_access = models.IntegerField()
    usrgrpid = models.ForeignKey('Usrgrp', db_column='usrgrpid', blank=True, null=True)
    groupid = models.ForeignKey(Groups, db_column='groupid', blank=True, null=True)
    description = models.TextField()
    confirmation = models.CharField(max_length=255)
    type = models.IntegerField()
    execute_on = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scripts'


class ServiceAlarms(models.Model):
    servicealarmid = models.BigIntegerField(primary_key=True)
    serviceid = models.ForeignKey('Services', db_column='serviceid')
    clock = models.IntegerField()
    value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'service_alarms'


class Services(models.Model):
    serviceid = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    status = models.IntegerField()
    algorithm = models.IntegerField()
    triggerid = models.ForeignKey('Triggers', db_column='triggerid', blank=True, null=True)
    showsla = models.IntegerField()
    goodsla = models.FloatField()
    sortorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'services'


class ServicesTimes(models.Model):
    timeid = models.BigIntegerField(primary_key=True)
    serviceid = models.ForeignKey(Services, db_column='serviceid')
    type = models.IntegerField()
    ts_from = models.IntegerField()
    ts_to = models.IntegerField()
    note = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'services_times'


class Sessions(models.Model):
    sessionid = models.CharField(primary_key=True, max_length=32)
    userid = models.ForeignKey('Users', db_column='userid')
    lastaccess = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Slides(models.Model):
    slideid = models.BigIntegerField(primary_key=True)
    slideshowid = models.ForeignKey('Slideshows', db_column='slideshowid')
    screenid = models.ForeignKey(Screens, db_column='screenid')
    step = models.IntegerField()
    delay = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slides'


class SlideshowUser(models.Model):
    slideshowuserid = models.BigIntegerField(primary_key=True)
    slideshowid = models.ForeignKey('Slideshows', db_column='slideshowid')
    userid = models.ForeignKey('Users', db_column='userid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slideshow_user'
        unique_together = (('slideshowid', 'userid'),)


class SlideshowUsrgrp(models.Model):
    slideshowusrgrpid = models.BigIntegerField(primary_key=True)
    slideshowid = models.ForeignKey('Slideshows', db_column='slideshowid')
    usrgrpid = models.ForeignKey('Usrgrp', db_column='usrgrpid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slideshow_usrgrp'
        unique_together = (('slideshowid', 'usrgrpid'),)


class Slideshows(models.Model):
    slideshowid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    delay = models.IntegerField()
    userid = models.ForeignKey('Users', db_column='userid')
    private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slideshows'


class SysmapUrl(models.Model):
    sysmapurlid = models.BigIntegerField(primary_key=True)
    sysmapid = models.ForeignKey('Sysmaps', db_column='sysmapid')
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    elementtype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmap_url'
        unique_together = (('sysmapid', 'name'),)


class SysmapUser(models.Model):
    sysmapuserid = models.BigIntegerField(primary_key=True)
    sysmapid = models.ForeignKey('Sysmaps', db_column='sysmapid')
    userid = models.ForeignKey('Users', db_column='userid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmap_user'
        unique_together = (('sysmapid', 'userid'),)


class SysmapUsrgrp(models.Model):
    sysmapusrgrpid = models.BigIntegerField(primary_key=True)
    sysmapid = models.ForeignKey('Sysmaps', db_column='sysmapid')
    usrgrpid = models.ForeignKey('Usrgrp', db_column='usrgrpid')
    permission = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmap_usrgrp'
        unique_together = (('sysmapid', 'usrgrpid'),)


class Sysmaps(models.Model):
    sysmapid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=128)
    width = models.IntegerField()
    height = models.IntegerField()
    backgroundid = models.ForeignKey(Images, db_column='backgroundid', blank=True, null=True)
    label_type = models.IntegerField()
    label_location = models.IntegerField()
    highlight = models.IntegerField()
    expandproblem = models.IntegerField()
    markelements = models.IntegerField()
    show_unack = models.IntegerField()
    grid_size = models.IntegerField()
    grid_show = models.IntegerField()
    grid_align = models.IntegerField()
    label_format = models.IntegerField()
    label_type_host = models.IntegerField()
    label_type_hostgroup = models.IntegerField()
    label_type_trigger = models.IntegerField()
    label_type_map = models.IntegerField()
    label_type_image = models.IntegerField()
    label_string_host = models.CharField(max_length=255)
    label_string_hostgroup = models.CharField(max_length=255)
    label_string_trigger = models.CharField(max_length=255)
    label_string_map = models.CharField(max_length=255)
    label_string_image = models.CharField(max_length=255)
    iconmapid = models.ForeignKey(IconMap, db_column='iconmapid', blank=True, null=True)
    expand_macros = models.IntegerField()
    severity_min = models.IntegerField()
    userid = models.ForeignKey('Users', db_column='userid')
    private = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sysmaps'


class Timeperiods(models.Model):
    timeperiodid = models.BigIntegerField(primary_key=True)
    timeperiod_type = models.IntegerField()
    every = models.IntegerField()
    month = models.IntegerField()
    dayofweek = models.IntegerField()
    day = models.IntegerField()
    start_time = models.IntegerField()
    period = models.IntegerField()
    start_date = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'timeperiods'


class Trends(models.Model):
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    num = models.IntegerField()
    value_min = models.FloatField()
    value_avg = models.FloatField()
    value_max = models.FloatField()

    class Meta:
        managed = False
        db_table = 'trends'
        unique_together = (('itemid', 'clock'),)


class TrendsUint(models.Model):
    itemid = models.BigIntegerField()
    clock = models.IntegerField()
    num = models.IntegerField()
    value_min = models.BigIntegerField()
    value_avg = models.BigIntegerField()
    value_max = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'trends_uint'
        unique_together = (('itemid', 'clock'),)

class Triggers(models.Model):
    triggerid = models.BigIntegerField(primary_key=True)
    expression = models.CharField(max_length=2048)
    description = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    status = models.IntegerField()
    value = models.IntegerField()
    priority = models.IntegerField()
    lastchange = models.IntegerField()
    comments = models.TextField()
    error = models.CharField(max_length=128)
    templateid = models.ForeignKey('self', db_column='templateid', blank=True, null=True)
    type = models.IntegerField()
    state = models.IntegerField()
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'triggers'


class Users(models.Model):
    userid = models.BigIntegerField(primary_key=True)
    alias = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=32)
    url = models.CharField(max_length=255)
    autologin = models.IntegerField()
    autologout = models.IntegerField()
    lang = models.CharField(max_length=5)
    refresh = models.IntegerField()
    type = models.IntegerField()
    theme = models.CharField(max_length=128)
    attempt_failed = models.IntegerField()
    attempt_ip = models.CharField(max_length=39)
    attempt_clock = models.IntegerField()
    rows_per_page = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersGroups(models.Model):
    id = models.BigIntegerField(primary_key=True)
    usrgrpid = models.ForeignKey('Usrgrp', db_column='usrgrpid')
    userid = models.ForeignKey(Users, db_column='userid')

    class Meta:
        managed = False
        db_table = 'users_groups'
        unique_together = (('usrgrpid', 'userid'),)


class Usrgrp(models.Model):
    usrgrpid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    gui_access = models.IntegerField()
    users_status = models.IntegerField()
    debug_mode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usrgrp'


class Valuemaps(models.Model):
    valuemapid = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'valuemaps'


class ScmDailyServerUsage(models.Model):
    date = models.DateField(primary_key=True)
    servertotalcount = models.IntegerField(db_column='ServerTotalCount', blank=True, null=True)  # Field name made lowercase.
    assignedservercount = models.IntegerField(db_column='AssignedServerCount')  # Field name made lowercase.
    servernotinusecount = models.IntegerField(db_column='ServerNotInUSeCount', blank=True, null=True)  # Field name made lowercase.
    usedratio = models.FloatField(db_column='UsedRatio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scm_daily_server_usage'

class ScmDailyServerUsageSeparate(models.Model):
    fid= models.IntegerField()
    date = models.DateField()
    servertotalcount = models.IntegerField(db_column='ServerTotalCount', blank=True, null=True)  # Field name made lowercase.
    region=models.CharField(unique=True, max_length=4)
    assignedservercount = models.IntegerField(db_column='AssignedServerCount')  # Field name made lowercase.
    servernotinusecount = models.IntegerField(db_column='ServerNotInUSeCount', blank=True, null=True)  # Field name made lowercase.
    usedratio = models.FloatField(db_column='UsedRatio', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'scm_daily_server_usage_separate'
           



class CompileDailyServerUsage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateField()
    normal_usage_server_count = models.IntegerField()
    low_usage_server_count = models.IntegerField()
    nearly_no_usage_server_count = models.IntegerField()
    high_usage_server_count = models.IntegerField()
    region = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'compile_daily_server_usage'



class CompileServerUsageInfo(models.Model):
    date = models.DateField(blank=True, null=True)
    hostname = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    ipaddress = models.CharField(max_length=255, blank=True, null=True)
    cpu_load_gt_50_coun = models.IntegerField(blank=True, null=True)
    total_memory = models.CharField(max_length=255, blank=True, null=True)
    total_cpu_cores = models.IntegerField(db_column='total_CPU_cores', blank=True, null=True)  # Field name made lowercase.
    largest_disk_mount_point = models.CharField(max_length=255, blank=True, null=True)
    total_diskspace = models.CharField(max_length=255, blank=True, null=True)
    used_diskspace = models.CharField(max_length=255, blank=True, null=True)
    disk_used_ratio = models.FloatField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'compile_server_usage_info'
