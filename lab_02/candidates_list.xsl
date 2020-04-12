<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
  <html>
  <body>
  <h2>Djinni.co Candidates List</h2>
  <table border="1">
    <tr bgcolor="#9acd32">
      <th>url</th>
      <th>position</th>
      <th>locations</th>
      <th>salary</th>
      <th>years_of_experience</th>
      <th>english_level</th>
      <th>experience</th>
      <th>skills</th>
      <th>highlights</th>
      <th>expectations</th>
    </tr>
    <xsl:for-each select="candidates/candidate">
    <tr>
      <td><xsl:value-of select="url"/></td>
      <td><xsl:value-of select="position"/></td>
      <td><xsl:apply-templates select="locations" /></td>
      <td><xsl:value-of select="salary"/></td>
      <td><xsl:value-of select="years_of_experience"/></td>
      <td><xsl:value-of select="english_level"/></td>
      <td><xsl:value-of select="experience"/></td>
      <td><xsl:apply-templates select="skills" /></td>
      <td><xsl:value-of select="highlights"/></td>
      <td><xsl:value-of select="expectations"/></td>
    </tr>
    </xsl:for-each>
  </table>
  </body>
  </html>
</xsl:template>
<xsl:template match="locations">
  <xsl:for-each select="value">
<xsl:value-of select="." />,
  </xsl:for-each>
</xsl:template>
  <xsl:template match="skills">
  <xsl:for-each select="value">
<xsl:value-of select="." />,
  </xsl:for-each>
</xsl:template>
</xsl:stylesheet>
