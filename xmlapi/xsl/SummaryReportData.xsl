<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:output method="text" encoding="UTF-8"/>

    <xsl:template match="/">
        <xsl:text>&#xA;</xsl:text>
        <xsl:for-each select="*">
            <xsl:value-of select="concat('&quot;', @app_name, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @app_id, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @business_unit, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @business_owner, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @build_id, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @submitter, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @generation_date, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @veracode_level, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="@total_flaws"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="@flaws_not_mitigated"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @last_update_time, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="@is_latest_build"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @policy_name, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="concat('&quot;', @policy_compliance_status, '&quot;')"/>
            <xsl:text>,</xsl:text>
            <xsl:value-of select="@scan_overdue"/>
            <xsl:text>&#xA;</xsl:text>
        </xsl:for-each>
    </xsl:template>

</xsl:stylesheet>

