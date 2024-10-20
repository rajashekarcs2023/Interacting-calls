import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Box, Card, CardContent, Typography, LinearProgress, Container, Divider } from '@mui/material';

const DistressDashboard = () => {
  const [distressData, setDistressData] = useState([]);
  const [summary, setSummary] = useState(null);
  const [city, setCity] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch all distress calls
    const fetchDistressCalls = async () => {
      try {
        const distressResponse = await axios.get('http://localhost:8000/distress_calls');
        const summaryResponse = await axios.get('http://localhost:8000/distress_summary');
        setDistressData(distressResponse.data);
        setSummary(summaryResponse.data.summarized_message);
        setCity(summaryResponse.data.city);
      } catch (error) {
        console.error("Error fetching data: ", error);
      } finally {
        setLoading(false);
      }
    };

    fetchDistressCalls();
  }, []);

  if (loading) {
    return (
      <Box display="flex" justifyContent="center" alignItems="center" minHeight="100vh">
        <Typography variant="h5">Loading distress data...</Typography>
      </Box>
    );
  }

  return (
    <Container maxWidth="md" style={{ marginTop: '50px' }}>
      <Typography variant="h3" align="center" gutterBottom>
        Distress Call Dashboard
      </Typography>

      {distressData.map((call, index) => (
        <Card key={index} style={{ display: 'flex', marginBottom: '20px', padding: '20px' }}>
          <Box style={{ flexGrow: 1 }}>
            <CardContent>
              <Typography variant="h6">Distress Call {index + 1}</Typography>
              <Typography variant="body2">
                <strong>Transcription:</strong> {call.transcription}
              </Typography>
              <Typography variant="body2">
                <strong>City:</strong> {call.city}
              </Typography>
              <Typography variant="body2">
                <strong>Distress Level:</strong> {call.distress_level}
              </Typography>
            </CardContent>
          </Box>
          <Box style={{ width: '250px', marginLeft: '20px' }}>
            {/* Distress Level Progress Bar */}
            <Typography variant="body2" align="center" style={{ marginBottom: '10px' }}>Distress Level</Typography>
            <LinearProgress variant="determinate" value={call.distress_level * 100} />
          </Box>
        </Card>
      ))}

      <Divider style={{ marginBottom: '30px' }} />

      {summary && (
        <Box>
          <Card style={{ padding: '20px', marginBottom: '30px' }}>
            <Typography variant="h5" color="primary" gutterBottom>
              Selected City: {city}
            </Typography>
            <Typography variant="body1">
              <strong>Dramatic Summary:</strong> {summary}
            </Typography>
          </Card>
        </Box>
      )}
    </Container>
  );
};

export default DistressDashboard;
